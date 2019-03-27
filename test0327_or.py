#!/usr/bin/python
# _*_ coding:UTF-8 _*_
'''
class Parent(object):
    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
'''
class Parent(object):
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implict()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD BEFORE PARENTaltered()"
        super(Child,self).altered()
        print "CHILD, AFTER PARENT altered()"
    
dad = Parent()
son = Child()

dad.altered()
son.altered()