import os
import tkinter as tk
path = "D:\\Study\\Uni\\Yr1"


def get_courses(path):
    Courses = os.listdir(path)
    return Courses