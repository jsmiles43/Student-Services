#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:07:29 2017

@author: josephmiles
"""

import HW9 as f, unittest

class repoTest(unittest.TestCase):

    def test_loadUserInfoInstructor(self):
        repo = f.Repository()
        repo.loadUserInfo('instructors.txt', 'I')
        self.assertTrue(len(repo.instructor_list) != 0)
        self.assertIsInstance(list(repo.instructor_list.values())[0], f.Instructor)
     
        
    def test_loadUserInfoStudent(self):
        repo = f.Repository()
        repo.loadUserInfo('students.txt', 'S')
        self.assertTrue(len(repo.student_list) != 0)
        self.assertIsInstance(list(repo.student_list.values())[0], f.Student)

    def test_loadGrades(self):
        repo = f.Repository()
        repo.loadUserInfo('instructors.txt', 'I')
        repo.loadUserInfo('students.txt', 'S')
        repo.loadGrades('grades.txt')
        self.assertTrue(len(repo.student_list['10103'].classes_taken) != 0)
        self.assertTrue(len(repo.instructor_list['98765'].courses_taught) != 0)

    def test_loadMajors(self):
        repo = f.Repository()
        repo.loadUserInfo('instructors.txt', 'I')
        repo.loadUserInfo('students.txt', 'S')
        repo.loadMajors('majors.txt')
        self.assertTrue(len(repo.major_dict.keys()) != 0)
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity = 2)