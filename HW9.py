#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:01:52 2017

@author: josephmiles
"""

import os
import collections
from prettytable import PrettyTable

class Repository:
    
    def __init__(self):
        self.student_list = collections.defaultdict(Student)
        self.instructor_list = collections.defaultdict(Instructor)
        self.major_dict = collections.defaultdict(set)
        
            
    
    def loadUserInfo(self, file_name, user_type):
        try:
            file = open(file_name, 'r')
        except FileNotFoundError:
            print('Can’t open,', file_name, 'current directory is', os.getcwd())
        else:
            for line in file:
                CWID, name, dept = line.strip().split('\t')  
                if user_type == 'S':
                    self.student_list[CWID] = Student(CWID, name, dept)
                elif user_type == 'I':
                    self.instructor_list[CWID] = Instructor(CWID, name, dept)
                
    def loadGrades(self, file_name):
        try:
            file = open(file_name, 'r')
        except FileNotFoundError:
            print('Can’t open,', file_name, 'current directory is', os.getcwd())
        else:
            for line in file:
                CWID, course_name, grade, i_CWID = line.strip().split('\t')
                self.student_list[CWID].classes_taken[course_name] = grade
                self.instructor_list[i_CWID].courses_taught[course_name] += 1
            
    def loadMajors(self, file_name):
        try:
            file = open(file_name, 'r')
        except FileNotFoundError:
            print('Can’t open,', file_name, 'current directory is', os.getcwd())
        else:
            for line in file:
                dept, course = line.strip().split('\t')
                self.major_dict[dept].add(course)
            for cwid in self.student_list:
                self.student_list[cwid].classes_left = self.major_dict[self.student_list[cwid].dept] - set(self.student_list[cwid].classes_taken.keys())
                

    def printRepo(self):
        print('Student Summary')
        table = PrettyTable()
        table.field_names = ['CWID', 'NAME', 'Completed Courses', 'Classes Left']
        table.align = 'l'
        for CWID in self.student_list:
            table.add_row([CWID, self.student_list[CWID].name, sorted((list(dict(self.student_list[CWID].classes_taken).keys()))), self.student_list[CWID].classes_left])
        print(table)
        
        print('Instructor Summary')
        table2 = PrettyTable(['CWID', 'NAME', 'Dept', 'Courses', 'Students'])
        table2.align = 'l'
        for CWID in self.instructor_list:
            for course in self.instructor_list[CWID].courses_taught.keys():
                table2.add_row([CWID, self.instructor_list[CWID].name, self.instructor_list[CWID].dept, course, self.instructor_list[CWID].courses_taught[course]])
       
        print(table2)
                
            
class User:
    
    def __init__(self, _CWID, _name, _dept):
        self.CWID = _CWID
        self.name = _name
        self.dept = _dept
        
class Student(User):
    '''An extension of the User Class to create student objects'''
    def __init__(self, _CWID, _name, _dept):
        super(Student, self).__init__(_CWID, _name, _dept)
        self.classes_taken = collections.defaultdict(str)
        self.classes_left = set()
        
class Instructor(User):
    '''An extension of the User Class to create instructor objects'''
    def __init__(self, _CWID, _name, _dept):
        super(Instructor,self).__init__(_CWID, _name, _dept)
        self.courses_taught = collections.defaultdict(int)

def main():
    repo = Repository()
    repo.loadUserInfo('instructors.txt', 'I');
    repo.loadUserInfo('students.txt', 'S');
    repo.loadGrades('grades.txt')
    repo.loadMajors('majors.txt')
    repo.printRepo()
    
    
main()  
    
    