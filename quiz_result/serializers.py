from rest_framework import serializers
from .models import QuizUser, UserAnswers


class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = ['question', 'answer']


class GetUserAnswersSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField(read_only=True)
    answer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserAnswers
        fields = ['question', 'answer']


class QuizUserSerializer(serializers.ModelSerializer):
    user_answers = UserAnswersSerializer(many=True)
    current_answer = GetUserAnswersSerializer(many=True, read_only=True)

    class Meta:
        model = QuizUser
        fields = ['id', 'user', 'quiz', 'user_answers', 'current_answer']

    def create(self, validated_date):
        user_answers_data = validated_date.pop('user_answers')
        quiz_user = QuizUser.objects.create(**validated_date)
        for u in user_answers_data:
            UserAnswers.objects.create(
                quiz_user=quiz_user,
                **u
            )
        return quiz_user



class GetQuizUserSerializer(serializers.ModelSerializer):
    user_answers = GetUserAnswersSerializer(many=True)
    current_answer = GetUserAnswersSerializer(many=True, read_only=True)

    class Meta:
        model = QuizUser
        fields = ['id', 'user', 'quiz', 'user_answers', 'current_answer']
        extra_kwargs = {
            'current_answer': {'read_only': True}
        }