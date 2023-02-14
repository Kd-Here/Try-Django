from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

# Create your views here.


from .forms import CourseModelForm
from .models import Course 

class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 


class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)


# Here we will do update operation it takes same as create but use update in object

class CourseUpdateView(CourseObjectMixin, View):
    template_name = "courses/course_update.html" # DetailView
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


# For create raw class you need to have 2 method first get &  post for adding
class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self,request, *args, **kwargs): #here we have sefl bcoz we inside of Class
        # When for seeing use get 
        form = CourseModelForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    
    def post(self,request,*args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        const = {'form':form}
        return render(request,self.template_name,const)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get(self,request,*args,**kwargs):
        context = {'object_list':self.queryset}
        return render(request,self.template_name,context)


class CourseView(CourseObjectMixin,View):
    template_name = 'courses/course_detail.html'
    def get(self,request,id=None, *args, **kwargs): #here we have sefl bcoz we inside of Class
        context = {}

        if id is not None:
            obj = get_object_or_404(Course,id=id)
            context['object'] = obj
        return render(request, self.template_name, context)
    
    def post(self,request,*args, **kwargs):
        return render(request,self.template_name,{})


def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})

