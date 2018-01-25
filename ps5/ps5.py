# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid;
        self.title = title;
        self.description = description;
        self.link = link;
        self.pubdate = pubdate;
        
    def get_guid(self):
        return self.guid;
    def get_title(self):
        return self.title;
    def get_description(self):
        return self.description;
    def get_link(self):
        return self.link;
    def get_pubdate(self):
        return self.pubdate;



#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower();

    def is_phrase_in(self, text):
        cleanText = "";
        for char in text.lower():
            #print(char);
            #print(string.punctuation.count(char))
            if string.punctuation.count(char) > 0:
                #print("hit!")
                cleanText += " ";
            else:
                cleanText += char;
            #print(cleanText);
        textList = cleanText.split();
        phraseList = self.phrase.lower().split();
        #print(textList);
        #print(phraseList);
        if textList.count(phraseList[0]):
            index = textList.index(phraseList[0]);
        else:
            return False;
        if index + len(phraseList) > len(textList):
            return False;
        for counter in range(len(phraseList)):
            if textList[index+counter] != phraseList[counter]:
                return False
        return True;

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase);
    
    def evaluate(self, story):
        return self.is_phrase_in(story.title);

#cuddly    = NewsStory('', 'The purple cow is soft and cuddly.', '', '', datetime.now())
#exclaim   = NewsStory('', 'Purple!!! Cow!!!', '', '', datetime.now())
#symbols   = NewsStory('', 'purple@#$%cow', '', '', datetime.now())
#spaces    = NewsStory('', 'Did you see a purple     cow?', '', '', datetime.now())
#caps      = NewsStory('', 'The farmer owns a really PURPLE cow.', '', '', datetime.now())
#exact     = NewsStory('', 'purple cow', '', '', datetime.now())
#plural    = NewsStory('', 'Purple cows are cool!', '', '', datetime.now())
#separate  = NewsStory('', 'The purple blob over there is a cow.', '', '', datetime.now())
#brown     = NewsStory('', 'How now brown cow.', '' ,'', datetime.now())
#badorder  = NewsStory('', 'Cow!!! Purple!!!', '', '', datetime.now())
#nospaces  = NewsStory('', 'purplecowpurplecowpurplecow', '', '', datetime.now())
#nothing   = NewsStory('', 'I like poison dart frogs.', '', '', datetime.now())
#
#s1 = TitleTrigger('PURPLE COW')
#s2  = TitleTrigger('purple cow')
#for trig in [s1, s2]:
#    print(trig.evaluate(cuddly))
#    print();
#    print(trig.evaluate(exclaim))
#    print();
#    print(trig.evaluate(symbols))
#    print();
#    print(trig.evaluate(spaces))
#    print();
#    print(trig.evaluate(caps))
#    print();
#    print(trig.evaluate(exact))
#    print();
#    
#    print(trig.evaluate(plural))
#    print();
#    print(trig.evaluate(separate))
#    print();
#    print(trig.evaluate(brown))
#    print();
#    print(trig.evaluate(badorder))
#    print();
#    print(trig.evaluate(nospaces))
#    print();
#    print(trig.evaluate(nothing))        


# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase);
    
    def evaluate(self, story):
        return self.is_phrase_in(story.description);

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time):
        self.datetime = datetime.strptime(time, "%d %b %Y %H:%M:%S");

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time);

    def evaluate(self, event):
#        eventTime = datetime.strptime(event.get_pubdate(), "%d %b %Y %H:%M:%S");
        #print(event.get_pubdate());
        #print(self.datetime);
        if event.get_pubdate() < self.datetime:
            return True;
        else:
            return False;
            
class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time);

    def evaluate(self, event):
#        eventTime = datetime.strptime(event.get_pubdate(), "%d %b %Y %H:%M:%S");
        if event.get_pubdate() > self.datetime:
            return True;
        else:
            return False;

#dt = timedelta(seconds=5)
#now = datetime(2016, 10, 12, 23, 59, 59)
#now = now.replace(tzinfo=pytz.timezone("EST"))
#        
#ancient_time = datetime(1987, 10, 15)
#ancient_time = ancient_time.replace(tzinfo=pytz.timezone("EST"))
#ancient = NewsStory('', '', '', '', ancient_time)
#        
#just_now = NewsStory('', '', '', '', now - dt)
#in_a_bit = NewsStory('', '', '', '', now + dt)
#
#future_time = datetime(2087, 10, 15)
#future_time = future_time.replace(tzinfo=pytz.timezone("EST"))
#future = NewsStory('', '', '', '', future_time)
#
#
#s1 = BeforeTrigger('12 Oct 2016 23:59:59')
#s2 = AfterTrigger('12 Oct 2016 23:59:59')
#
#print(s1.evaluate(ancient))
#print(s1.evaluate(just_now))
#
#self.assertFalse(s1.evaluate(in_a_bit), "BeforeTrigger fired to fire on news happened right after specified time")
#self.assertFalse(s1.evaluate(future), "BeforeTrigger fired to fire on news from the future")
#
#self.assertFalse(s2.evaluate(ancient), "AfterTrigger fired to fire on news from long ago")
#self.assertFalse(s2.evaluate(just_now), "BeforeTrigger fired to fire on news happened right before specified time")
#
#self.assertTrue(s2.evaluate(in_a_bit), "AfterTrigger failed to fire on news just after specified time")
#self.assertTrue(s2.evaluate(future), "AfterTrigger failed to fire on news from long ago")
            
# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, T):
        self.other = T;
        
    def evaluate(self, content):
        return not self.other.evaluate(content);

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.other1 = T1;
        self.other2 = T2;
    
    def evaluate(self, content):
        return self.other1.evaluate(content) and self.other2.evaluate(content);

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.other1 = T1;
        self.other2 = T2;
    
    def evaluate(self, content):
        return self.other1.evaluate(content) or self.other2.evaluate(content);

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    storiesList = [];
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                storiesList.append(story);
                break;
    return storiesList;


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    triggers = {};
    returning = [];
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    dic = {'TITLE': TitleTrigger, 'DESCRIPTION': DescriptionTrigger, 'AFTER': AfterTrigger, 'BEFORE': BeforeTrigger, 'NOT': NotTrigger, 'AND': AndTrigger, 'OR': OrTrigger};
    for line in lines:
        line = line.split(",")
        #print(line);
        if "AND OR And Or and or".count(line[1]):
            triggers[line[0]] = dic[line[1]](triggers[line[2]], triggers[line[3]]);
        elif "NOT Not not".count(line[1]):
            triggers[line[0]] = dic[line[1]](triggers[line[2]]);
        elif line[0] == "ADD":
            for name in line[1:]:
                returning.append(triggers[name]);
        else:
            triggers[line[0]] = dic[line[1]](line[2]); 
    return returning; # for now, print it so you see what it contains!
#read_trigger_config("triggers.txt");


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))
            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()