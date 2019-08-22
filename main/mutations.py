from graphene_django.forms.mutation import DjangoModelFormMutation
from main.types import UserType,ProfileType,PostType,CommentType
from main.models import User,Profile,Post,Comment
from main.forms import UserForm,ProfileForm,PostForm,CommentForm
from graphene import Field,AbstractType




class PostMutation(DjangoModelFormMutation):
    post = Field(PostType)

    # @classmethod
    # def perform_mutate(cls, form, info):
    #     post_obj = form.save()
    #     try:
    #         image = info.context.FILES['file']
    #         blog_obj.image = image
    #         blog_obj.save()
    #         kwargs = {cls._meta.return_field_name: blog_obj}
    #         return cls(errors=[], **kwargs)
    #     except:
    #         kwargs = {cls._meta.return_field_name: blog_obj}
    #         return cls(errors=[], **kwargs)

    class Meta:
        form_class = PostForm


class CommentMutation(DjangoModelFormMutation):
    comment = Field(CommentType)

    class Meta:
        form_class = CommentForm


class ProfileMutation(DjangoModelFormMutation):
    profile = Field(ProfileType)

    class Meta:
        form_class = ProfileForm


class UserMutation(DjangoModelFormMutation):
    user = Field(UserType)

    @classmethod
    def perform_mutate(cls, form, info):
        obj = form.save()
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        kwargs = {cls._meta.return_field_name: obj}
        return cls(errors=[], **kwargs)


    class Meta:
        form_class = UserForm

class Mutation(AbstractType):
    create_post = PostMutation.Field()
    create_comment = CommentMutation.Field()
    create_profile = ProfileMutation.Field()
    create_user = UserMutation.Field()