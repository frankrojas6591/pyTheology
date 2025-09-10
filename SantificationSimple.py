'''
'''
## Step 1: Defining basic element and objects of the event


class energy(object):
  def __init__(self, **kwargs):
    self.num = self.__class__.__name__
    self.creator = kwargs.get('creator', None)
    self.energy = kwargs.get('power', 'finite')
                             
class event(object):
  def __init__(self, action=Minor, **kwargs):
    self.super().__init__(**kwargs)
    self.action = action
    self.actor = kwargs.get('actor', None)
    self.victim = kwargs.get('victim', None)

class judgement(event):
  def __init__(self, **kwargs):
    self.super.__init__(**kwargs)
    # prudence is a quality of a person's judgement
    #    awareness of God's Will:  acting with or showing care and thought for the future.
    # 0 :: ignorant of God's will
    # <0 :: not aligned with God's will [-100 to -1]
    # >0 :: aligned with God's will
    self.prudence = kwargs.get('prudence', 0)
    
class GOD(energy):
  def __init__(self, creator = GOD(), power = 'finite', **kwargs):
    self.super.__init__(**kwargs)
    self.energy = 'infinite'

  def GodJudgement(self, person, event, J):
    J_GW = 'judgement aligned with Gods Will'
    # compute personal santificatication_score 
    God_score = J_GW - J
    return God_score

class kingdom(energy):        
  def __init__(self, **kwargs):
    self.super.__init__(**kwargs)
    
class reason(event):
  def __init__(self, desc = 'love', **kwargs):
    self.super.__init__(**kwargs)
    self.desc = desc

class intellect(event):
  def __init__(self, , action = 'love', **kwargs):
    self.super.__init__(**kwargs)
    self.knowledge = event(action='educate', desc=kwargs.get('desc','minorLesson'))    

class person(energy):
  def __init__(self, **kwargs):
    self.super.__init__(**kwargs)
    self.name = self
    self.God = God
    # track every event in life of person
    self.eventList = [event(creator='God', 
                            action='createHuman',
                            reason = reson)]
    # track all knowledge, lessons of life
    self.intellectList = []
    self.reasonList = [reason(creator='God',prudence='risky')]

  def addEvent(self, event):
    self.eventList.append(event)
  def addKnowledge(self, intellect):
    self.intellectList.append(intellect)
    
  def death(self):
    God = self.creator
    
    # Compute a person's life time santification score 
    #   - for every event in a person's life (eventList)
    #   - compute human judgement score
    #   - compute God judgement score
    #   - sum of a all events, ie. alignment with God's will
    santification_score = 0
    for event in self.eventList:
      J = judgement(event)
      santification_score  += self.creator.GodJudgement(event, J)
    self.santification_score = santificsation_score 

  def santification(self):
      J = HumanJudgement(event, reason, intellect)
      add event to history of person's intellect
      GodJudgement(person)
    
God = GOD(energy='infinie')
Heaven = kingdom(creator=God, energy='infinite')
Earth = thing(creator=God)
human = person(creator=God)



  


def HumanJudgement(event, reason, intellect):
      personal_Judgement = discern event in light of person's reason and intellect and relationship with God
      if event included another child of God 
            apply penalty to personal_Judgement for judgement of others
      return personal_Judgement


#### Step 2: Ask user to describe an event

## Step 3: Person passes judgement on the event

## Step 4: Assess the human judgement 

## Step 5: Record the human judgement 
- add to santification history
- add to person's intellect history
- add to person's reasonng history

## Step 6: Repeat more events

## Step 7: Death, God's judgement 
- calculate santification score for enterance into the kingdom
