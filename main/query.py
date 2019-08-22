from main.types import UserType,ProfileType,PostType,CommentType
from main.models import User,Profile,Post,Comment
import graphene


class Query(object):
    profile = graphene.List(ProfileType,id=graphene.ID())
    posts = graphene.List(PostType)
    post = graphene.List(PostType,id=graphene.ID())
    comments = graphene.List(CommentType)
    user = graphene.List(UserType)

    def resolve_post(self,info,id=None):
        # print(dir(graphene))
        # print('c')
        if id is not None:
            return Post.objects.filter(id=id)
        return Post.objects.all()


    def resolve_posts(self,info,**kwargs):
        return Post.objects.all()

    def resolve_commets(self,info,**kwargs):
        return Comment.objects.all()

    def resolve_user(self,info,**kwargs):
        return User.objects.all()
        
    def resolve_profile(self,info,id=None):
        if id is not None:
          return Profile.objects.filter(id=id)
        return Profile.objects.all()