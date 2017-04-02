#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:07:29 2017

@author: josephmiles
"""

import HW9 as f, unittest

class repoTest(unittest.TestCase):
    def test_finduser(self):
        repo = f.Repository()
        repo.instructor_list = [f.Instructor('98560', 'A', 'SSW') , f.Instructor('98561', 'B', 'SSB'), f.Instructor('98562', 'C', 'SSA')]
        self.assertTrue(repo.findUser('98560'))
        self.assertTrue(repo.findUser('98561'))
        self.assertFalse(repo.findUser('98559'))

    def test_loadUserInfoInstructor(self):
        repo = f.Repository()
        repo.loadUserInfo('instructors.txt', 'I')
        self.assertTrue(len(repo.instructor_list) != 0)
        self.assertIsInstance(repo.instructor_list[0], f.Instructor)
    
        
    def test_loadUserInfoStudent(self):
        repo = f.Repository()
        repo.loadUserInfo('students.txt', 'S')
        self.assertTrue(len(repo.student_list) != 0)
        self.assertIsInstance(repo.student_list[0], f.Student)

    def test_loadGrades(self):
        repo = f.Repository()
        repo.loadUserInfo('instructors.txt', 'I')
        repo.loadUserInfo('students.txt', 'S')
        repo.loadGrades('grades.txt')
        self.assertTrue(len(repo.student_list[0].classes_taken) != 0)
        self.assertTrue(len(repo.instructor_list[0].courses_taught) != 0)

        
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity = 2)