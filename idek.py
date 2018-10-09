import math
import setup
import RoboPiLib as RPL

s_pin = 1
e_pin = 0



RPL.servoWrite(s_pin,0)
RPL.servoWrite(e_pin,0)


d_one = 12 # this is the distance from shoulder to elbow
d_two = 14 # distance from elbow to wrist
sqd_one = math.pow(d_one, 2)
sqd_two = math.pow(d_two, 2)

while True:
    print 'Enter x value'
    x = input('- ') # given x input- how we tell robot where to go
    print 'Enter y value'
    y = input('- ') # given y input- how we tell robot where to go


    ###

    d_three = math.sqrt(math.pow(y, 2) + math.pow(x, 2)) # determining distance from shoulder to wrist
    sqd_three = math.pow(d_three, 2)
    a_three = math.acos((sqd_one + sqd_two - sqd_three) / (2 * d_one * d_two)) # angle of elbow using law of cosines
    a_two = math.asin((d_two * math.sin(a_three)) / d_three) # angle between shoulder and wrist (put in a try?)
    a_one = 2 * math.pi - (a_three + a_two) # angle between elbow and shoulder (dont really need)
    a_four = math.atan(y / x) # angle between 0 line and wrist

    a_shoulder = a_four + a_two # angle the shoulder joint should be at from the 0 line
    a_elbow = a_three # elbow angle, flush back to shoulder is 0

    ###


    print a_shoulder

    def shoulder(a):
        a = (a * 2000 / math.pi) + 400  # fix ratios! right now 2000steps ~ 90° but not according to this
        RPL.servoWrite(s_pin, a)


    print a_elbow

    def elbow(a):
        a = (a * 6000 / math.pi) + 400
        RPL.servoWrite(s_pin, a)

    if 400 < a_shoulder < 2000 # check these numbers - making sure it only tries to go to angles it can. shoulder is more limited than elbow
        shoulder(a_shoulder)
    else:
        print "Shoulder angle is unreachable."

    if 400 < a_elbow < 2000
        elbow(a_elbow)
    else:
        print "Elbow angle is unreachable."
