import pyttsx3


engine = pyttsx3.init()
# engine.say('''My grade school self did something evil to make sure that I was never bullied again''')
# engine.runAndWait()


# engine.say('''I was diagnosed with aspergers when I was 6 years old and had to be trained by a speech therapist to talk properly. As I was growing up, I was an outcast for liking geeky things and not exactly fitting in with the rest of the class.

# The bullying wasn't super bad, but they definitely underestimated my intelligence and ability to observe my surroundings.

# Now, there came a time when my school was hosting a grade-wide soccer tournament. I loved being the goalie, and was actually good at is as a grade-schooler, and I put myself on the sign-up list. The teams were randomly selected, and I was selected to be on a team as a goalie!

# However, it was very clear that my teammates didn't want me on their team, and they made it obvious that they didn't like me and thought that I would lose them the game if I was on their team.

# Then, the next day, my name was sketched out on the teams list and had defaming graffiti all over it. I was, of course, very sad, and the teachers, parents, and principal got involved and punished the boys heavily for what happened.

# Afterwards, I was placed on a different team with people that accepted me and were kind to me, and believe it or not, thanks in part to the fact that I never let a single goal through except for the final game, we won in a shoot out and won the school-wide tournament.

# Yet to this day, it was never discovered who did the graffiti on me, but since my team won everyone figured that all was well and that no one had a reason to bully me again.

# But there's a reason that graffiti artist was never found...

# It was me.

# While no one was looking, I defamed and destroyed my own name on the sign-up list knowing that those that were bullying me would get into trouble. Then, when it was discovered by teachers, everyone immediately assumed it was one of the bullies and that I had every right to be sad because of what happened...

# But not a single soul to this day knows that I defamed myself for the purpose of making sure I was never bullied again.

# TL:DR; A school soccer team I was assigned on didn't like me at all and was bullying me, so I graffiti'd my own name on the roster sheet to get my bullies in trouble. Then my team won the tournament and no one at the school bullied me ever again!''')
# engine.runAndWait();

# engine.save_to_file('Hello World', 'test.mp3')


with open('title.txt') as titleFile:
	title = titleFile.read()

	print('read title')

with open('text.txt') as textFile:
	text = textFile.read()

	print('read text')


engine.save_to_file(title, 'try5.wav')
engine.runAndWait()

print('all done')

