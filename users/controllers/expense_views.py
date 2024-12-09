from django.db.models import Sum
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, \
    GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response

from users.models import Expense
from users.serializers.expense_serializers import ExpenseSerializer, ExpenseCreateSerializer, \
    ExpensePartialUpdateSerializer, ExpenseByDateRangeSerializer, ExpenseSummarySerializer, CategorySummarySerializer


class ExpenseListAPIView(ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = permissions.AllowAny,
    queryset = Expense.objects.all()


class ExpenseCreateAPIView(CreateAPIView):
    serializer_class = ExpenseCreateSerializer
    permission_classes = permissions.AllowAny,
    queryset = Expense.objects.all()


class ExpenseUpdateAPIView(UpdateAPIView, UpdateModelMixin):
    permission_classes = permissions.AllowAny,
    serializer_class = ExpensePartialUpdateSerializer
    queryset = Expense.objects.all()

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ExpenseRetrieveAPIView(RetrieveAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


class ExpenseDestroyAPIView(DestroyAPIView):
    permission_classes = permissions.AllowAny,
    queryset = Expense.objects.all()


class ExpenseByDateRangeAPIView(ListAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = ExpenseByDateRangeSerializer

    def get_queryset(self):
        params = self.request.query_params
        return Expense.objects.filter(
            date__range=[params.get('start_date'), params.get('end_date')], user=params.get('user'))

    @swagger_auto_schema(
        operation_description="List all expenses for a user within a specific date range.",
        manual_parameters=[
            openapi.Parameter('user', openapi.IN_QUERY, description="User ID", type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Start Date (YYYY-MM-DD)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, required=True),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="End Date (YYYY-MM-DD)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, required=True),
        ],
        responses={
            200: openapi.Response("Status ok", ExpenseByDateRangeSerializer),
            400: openapi.Response(description="Invalid parameters")
        }
    )
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if page := self.paginate_queryset(queryset):
            serializer = ExpenseSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(ExpenseSerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class ExpenseSummaryAPIView(GenericAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = ExpenseSummarySerializer

    @swagger_auto_schema(
        operation_description="Calculate and return the total expenses per category for a given month.",
        manual_parameters=[
            openapi.Parameter('user', openapi.IN_QUERY, description="User ID", type=openapi.TYPE_INTEGER,
                              required=True),
            openapi.Parameter('year', openapi.IN_QUERY, description="Year number, example: 2024",
                              type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('month', openapi.IN_QUERY, description="Month number from 1-12",
                              type=openapi.TYPE_INTEGER, required=True),
        ],
        responses={
            200: openapi.Response("Status ok", CategorySummarySerializer),
            400: openapi.Response(description="Invalid parameters")
        }
    )
    def get(self, request, *args, **kwargs):
        data = self.serializer_class(data=request.query_params)
        data.is_valid(raise_exception=True)
        validated_data = data.validated_data
        return Response(CategorySummarySerializer(Expense.objects.filter(
            user=validated_data.get('user'), date__year=validated_data.get('year'),
            date__month=validated_data.get('month')
        ).values('category').annotate(total_amount=Sum('amount')), many=True).data, status=status.HTTP_200_OK)
