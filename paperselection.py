import os
import tkinter as tk
path = os.getcwd()
path = os.path.join(path,"Class_Materials")


def get_courses(path):
    Courses = os.listdir(path)
    return Courses