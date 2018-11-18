# inverse kinematics take 1!
# math syntax: https://docs.python.org/2/library/math.html
import math
import fractions
import sys

d_one = 20 # the distance from shoulder to elbow


print "Enter wanted angle in degrees"
angle = input('- ')

angle = angle * math.pi / 180

y = d_one * math.sin(angle)
x = d_one * math.cos(angle)

print x
print y

a_four = math.atan2(y , x)
print a_four * 180/math.pi
