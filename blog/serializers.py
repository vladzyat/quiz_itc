from rest_framework import serializers
from .models import Quiz, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    # question = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'title', 'correct', 'question')


class GetAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'title')


class QuestionSerializer(serializers.ModelSerializer):
    question_answers = GetAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'quiz', 'count_answers', 'count_correct_answers', 'question_answers')


class GetQuestionSerializer(serializers.ModelSerializer):
    question_answers = GetAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'quiz', 'question_answers')


class QuizSerializer(serializers.ModelSerializer):
    quiz_questions = GetQuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'description', 'count_questions', 'quiz_questions')