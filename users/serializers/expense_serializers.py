from rest_framework import serializers
from users.models import Expense, User


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Expense
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('Amount must be positive')
        return value


class ExpensePartialUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    amount = serializers.IntegerField(required=False)
    category = serializers.CharField(required=False)

    class Meta:
        model = Expense
        exclude = 'user', 'date',

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('Amount must be positive')
        return value


class ExpenseByDateRangeSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    user = serializers.IntegerField()


class ExpenseSummarySerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def validate_month(self, value):
        if value < 1 or value > 12:
            raise serializers.ValidationError('Month must be between 1 and 12')
        return value

    def validate_year(self, value):
        if value < 0:
            raise serializers.ValidationError('Year must be positive')
        return value


class CategorySummarySerializer(serializers.Serializer):
    category = serializers.CharField()
    total_amount = serializers.IntegerField()
