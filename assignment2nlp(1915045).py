Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
os.getcwd()
'C:\\Program Files\\Python310'
import re
openfile = open("", 'r')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    openfile = open("", 'r')
FileNotFoundError: [Errno 2] No such file or directory: ''
openfile = open("art1.dat", 'r')
contents = openfile.read()
contents
'Ringgit to strengthen against US dollar.\nThe US dollar-Ringgit exchange rate is forming a death-cross pattern, which in the past has led to a decline in the currency pair, based on technical charts. \nBloomberg reported on Wednesday that this death-cross pattern occurs when a 50-day moving average drops below the 100-day gauge. \nIt said on the previous three occasions this move took place, the dollar posted additional losses of 3%, 3% and 7% before finding a bottom. \nThe ringgit has underperformed Asian currencies since policy makers took steps in November to deter foreign banks from trading non-deliverable forwards, the wire report said.\nAt 1.45pm, the ringgit was trading at 4.4305 to the dollar from the previous close of 4.4312.\n'
openfile2 = open("art2.dat", 'r')
contents = openfile.read()
contents
SyntaxError: multiple statements found while compiling a single statement
contents = openfile.read()
contents
''
contents2 = openfile2.read()
contents2
"US trade deficit falls from two-year high on weak imports.\nThe U.S. trade deficit fell from a near two year high in February as slowing domestic demand weighed on imports and stronger global growth boosted exports of American goods.\nThe politically sensitive trade gap with China narrowed sharply by 26.6 percent from January to $23 billion ahead of a summit between President Donald Trump and China's Xi Jinping this week, although seasonal factors were likely behind the dramatic drop, economists said.\nThe Commerce Department said on Tuesday the trade deficit declined 9.6 percent to $43.6 billion, also as exports increased to their highest level in more than two years, after rising to a near two-year high of $48.2 billion in January.\n"
openfile3 = open("art3.dat", 'r')
contents3 = openfile3.read()
contents3
"No survivors: Malaysian mixed doubles all out of Malaysia Open\nNational No 1 mixed doubles Chan Peng Soon-Goh Liu Ying were sent home early, after crashing out in the first round of the Malaysia Open on Wednesday.\nThe 2016 Rio Olympic Games silver medallists failed to retain their momentum after winning the first game 21-18 against Indonesian duo Edi Subaktiar-Gloria Emanuelle Widjaja, losing the remaining two sets 21-19, 21-17.\nThe defeat was the second major blow for the national camp, following the first round exit of former men's doubles world No 1 Goh V Shem-Tan Wee Kiong who went down 21-17, 23-21 to Or Chin Chung-Tang Chun Man of Hong Kong.\nTwo other pairs Hoo Pang Ron-Peck Yen Wei and Tan Kian Meng-Lai Pei Jing also failed to deliver, ending Malaysia's interest in the mixed doubles.\nPang Ron-Peck Wei lost 22-20, 21-16 to South Korea's Choi Solgyu-Chae Yoo Jung, while Kian Meng-Pei Jing succumbed 6-21, 21-19, 21-13 to Japan's Kenta Kazuno-Ayane Kurihara.\nNational No 3 Goh Soon Huat-Shevon Lai Jemie had conceded a walkover earlier after the former injured himself during training on Tuesday."
openfile4 = open("art4.dat", 'r')
contents4 = openfile4.read()
contents4
'Ibrahimovic saves Man Utd, Leicester surge on.\nZlatan Ibrahimovic marked his return from suspension with a 94th-minute penalty to earn Manchester United a 1-1 draw against Everton at Old Trafford on Tuesday.\nA deliberate handball by Ashley Williams, who was sent off, allowed Ibrahimovic to cancel out Phil Jagielka’s opener and extend United’s unbeaten run in the Premier League to 20 matches.\nBut it remained an unwelcome result for Jose Mourinho’s side, who have now drawn nine games at home this season and trail fourth-place Manchester City by four points.\nElsewhere, Leicester City’s resurgence under Craig Shakespeare continued as they beat bottom club Sunderland 2-0 to record a sixth successive win since the dismissal of manager Claudio Ranieri.\nIbrahimovic’s last-gasp spot-kick – his 27th goal of the season – meant United held on to fifth place, three points above Arsenal and Everton having played a game more than the former.'
openfile5 = open("art5.dat", 'r')
contents5 = openfile5.read()
contents5
'Federer blows past del Potro into Miami fourth round.\nIn-form Roger Federer powered his way into the fourth round of the Miami Open with a 6-3 6-4 win over Argentina\'s Juan Martin del Potro on Monday.\nDel Potro always enjoys plenty of crowd support in Miami, which has a large Argentine community, and it was the same story again with football-style chants of support ringing out for the 28-year-old on a packed Crandon Park centre court.\nIt was the pair\'s first meeting since 2013 and having won 15 of the previous 21 encounters, Federer was favourite - but the crowd factor gave the third round match an added edge.\n"Shortly before I walked out to the court you could sense the atmosphere. That\'s when I told myself, Just be prepared for something different, you know. It was different," Federer said.\nHe was forced to save four break points in the first set but he got ahead with a thundering forehand to take a 5-3 lead and served out for the set.'
openfile6 = open("art6.dat", 'r')
contents6 = openfile6.read()
contents6
'Royals join memorial service for London terror attack victims.\nPrince William, his wife Kate and his brother Prince Harry spoke with survivors and the families of those killed in the terror attack outside the British parliament at a memorial service on Wednesday.\nThe royals joined those affected by the assault at a "Service of Hope" at Westminster Abbey, just across Parliament Square from the scene of the attack on March 22.\nThe assault killed four people, including a police officer guarding the gates of parliament.\nKhalid Masood, a 52-year-old convert to Islam known to the security services, drove into pedestrians on Westminster Bridge before stabbing policeman Keith Palmer to death. Masood was later shot and killed by officers in the parliament’s forecourt.\nLeslie Rhodes, 75, a retired window cleaner; Aysha Frade, 44, a school administrator; and Kurt Cochran, 54, an American tourist, were killed on the bridge.'
import nltk
import string

from collections import Counter
def get_tokens():
    opfile1 = open("covid1.dat", 'r') as article
    
SyntaxError: invalid syntax
def get_tokens():
    opfile1 = open("covid1.dat", 'r') as article:
        
SyntaxError: invalid syntax
def get_tokens():
    opfile1 = open('covid1.dat', 'r') as article:
        
SyntaxError: invalid syntax
def get_tokens():
    opfile1 = open('covid1.dat', 'r')
    text1 = opfile1.read()
    lowers = text1.lower()
    no_punct = nltk.word_tokenize(no_punct)
    nopunct = lowers.translate(string.punctuation)
    tokens = nltk.word_tokenize(nopunct)
    return tokens
tokens = get_tokens()
SyntaxError: invalid syntax









import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    from sklearn.feature_extraction.text import TfidfVectorizer
ModuleNotFoundError: No module named 'sklearn'
from sklearn.feature_extraction.text import TfidfVectorizer
documentA = 'the man went out for a walk'
documentB = 'the children sat around the fire'
bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1

numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    for word in bagOfWordsB:
from nltk.corpus import stopwords
SyntaxError: expected an indented block after 'for' statement on line 2
for word in bagOfWordsB:
    numOfWordsB[word] += 1
from nltk.corpus import stopwords
SyntaxError: invalid syntax
for word in bagOfWordsB:
    numOfWordsB[word] += 1

from nltk.corpus import stopwords
stopwords.words('english')
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
opfile1 = open('covid1.dat', 'r')
text1 = opfile1.read()
bagOfWordsC = text1.split(' ')
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))


































opfile2 = open('covid2.dat', 'r')
text2 = opfile2.read()
opfile3 = open('covid3.dat', 'r')
text3 = opfile3.read()
opfile4 = open('covid4.dat', 'r')
text4 = opfile4.read()
opfile5 = open('covid5.dat', 'r')
text5 = opfile5.read()
opfile6 = open('covid6.dat', 'r')
text6 = opfile6.read()
bagOfWordsFile1 = text1.split(' ')
bagOfWordsFile2 = text2.split(' ')
bagOfWordsFile3 = text3.split(' ')
bagOfWordsFile4 = text4.split(' ')
bagOfWordsFile5 = text5.split(' ')
bagOfWordsFile6 = text6.split(' ')
uniqueWordsFile = set(bagOfFile1).union(set(bagOfWordsFile2)).union(set(bagOfWordsFile3)).union(set(bagOfWordsFile3)).union(set(bagOfWordsFile4)).union(set(bagOfWordsFile5)).union(set(bagOfWordsFile6))
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    uniqueWordsFile = set(bagOfFile1).union(set(bagOfWordsFile2)).union(set(bagOfWordsFile3)).union(set(bagOfWordsFile3)).union(set(bagOfWordsFile4)).union(set(bagOfWordsFile5)).union(set(bagOfWordsFile6))
NameError: name 'bagOfFile1' is not defined
uniqueWordsFile = set(bagOfWordsFile1).union(set(bagOfWordsFile2)).union(set(bagOfWordsFile3)).union(set(bagOfWordsFile3)).union(set(bagOfWordsFile4)).union(set(bagOfWordsFile5)).union(set(bagOfWordsFile6))
numOfWordsFile1 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsFile1:
    numOfWordsFile1[word] += 1

Traceback (most recent call last):
  File "<pyshell#120>", line 2, in <module>
    numOfWordsFile1[word] += 1
KeyError: 'Mental'
print(uniqueWordsFile)
{'', 'build', 'NPIs', 'multiple', 'by', 'CI,', 'the', 'balanced', 'prevalence', 'patients', 'derived', 'largest', 'diabetes,', 'over', 'group', '294', '1,230', 'delta', 'Neural', 'veterans', 'hyperinflammatory', 'features', 'symptoms', '(February', 'depression,', 'prediction,', 'United', 'regarding', "ResNet50's", 'surveillance', 'October', 'tested', 'outpatient', 'US', 'critical', 'are', 'elevated', 'among', 'pneumonia.', 'were', 'IL-6', 'disorders', 'criteria', 'pipeline', 'outbreaks', 'real-time,', 'assessing', 'less', 'acute', 'rapid', 'and', 'Learning', 'stress', 'SARS-CoV-2,', 'The', 'tracing.', 'could', 'pre-existing', 'remaining', 'environment.', 'university', 'feelings', 'reduce', 'Mel', 'departments', 'branching', 'larger', 'greater', 'tracing,', 'men', 'Diagnosis', 'chest', 'universities', 'Association', 'environment.\n\nThe', 'collection', 'transmission', 'from', 'November', 'subthreshold', 'Disease', 'helpless,', 'between', 'trained', 'AY2021-2022.', 'previously', 'assess', 'quitting', 'signalling', 'contact', '(IL)-6', 'biomarker', 'simple', 'Since', 'presenting', 'a', 'Pediatric', 'COVID-19,', 'intensive', 'year', 'blockade', 'cytokines', 'therapeutic', 'then', 'PTS,', 'therapy', 'Departments.\n\nBetween', 'asymptomatics,', 'Cepstral', '(41%;', 'in', 'measured', 'has', 'depending', 'concentrations', 'At', 'Cough', 'finally', 'high', 'conflicting', 'binary', 'leverages', 'proportion', 'mental', '(PTS)', 'architecture', 'fear', 'Using', 'pandemic', 'infected', 'Coronavirus', 'feeling', 'found', 'to', 'Prediction', 'radiographs', '2021).', 'RF', 'halt', 'factors', 'framework', '5,320', 'steep', 'Boruta', 'MIT', 'offer', 'greatly', 'resulting', 'alcohol', 'CNN-based', 'one', 'increases', 'yielded', 'we', 'experiences.', 'into', 'explainable', 'presymptomatic', 'suggest', 'dataset', 'health', '35-47%).', 'testing.', 'data', 'dying,', 'asymptomatic', 'Women', 'noted', 'who', 'improving', 'saliency', 'isolation', 'pruned', 'recordings', 'with', 'PTSD', 'use', '(eg,', 'characteristic', 'rules', 'Experiences.\n\nPosttraumatic', 'presence', 'Machine', 'Open', 'important', 'As', 'University).', 'non-invasively,', 'risk', 'quick', 'additional', 'need', 'patient', 'Assessment', 'loved', 'people', 'architecture.', 'validated', 'Hopkins', '(AY);', '95%', 'or', 'learn', 'healthy,', 'acoustic', 'cross-validation', 'Namong', 'reliable', 'interventions', 'consequence,', 'secondarily', 'infecting', 'accurately', 'January', 'may', 'coronavirus', 'Care', 'fears', 'than', 'personalized', 'UC', 'achieve', 'significantly', 'created', 'compared', 'pre-pandemic', 'Poisson', 'hospitalisation', 'Who,', 'trajectories', 'States.', 'is', 'Among', '2020-2021', 'but,', 'through', 'process', 'relevant', 'control:', 'Berkeley', 'train', 'results,', 'anxiety', 'negative', 'associative', 'agent', 'continue', 'pre-trained', 'hyperarousal', 'developed', '(opensigma.mit.edu)', 'immunosuppression', 'isolation,', 'but', 'To', 'describe', 'admitted', 'testing', '20%', 'produce', 'discrimination', 'associated', 'continued', 'symptom', 'support', 'COVID-19.\n\nThe', 'Early', '81%', 'approaches', '2020)', 'minority', 'Emergency', 'explored', 'respiratory', 'provide', 'Optimizing', 'essentially', 'simplified,', 'extractors', 'affected', 'its', 'outbreak', 'what,', 'models', 'predominant', 'American', 'Veterans', '(SARS-CoV-2)', 'Checklist-', 'study', 'efforts', 'care', 'infected,', 'May', 'recording', 'including', 'map', 'based', 'ongoing,', 'COVID-19', 'Prevalence', 'audio', 'being', '4256', 'risk.', 'subjects,', 'Demographic', 'interleukin', 'decision', 'on', 'disorder', 'had', 'extracting', 'April', 'diagnostic.', '10-fold', 'young,', 'primarily', 'survey', 'was', 'Transfer', 'individual', 'positive', 'model', 'antibodies', 'Random', 'rising', 'COVID-19.', 'whom', 'an', 'when:effective', 'causative', 'benefit', '<', 'next', 'for', 'pandemic,', 'events', 'successfully', 'severe', 'cannabis', 'some', 'phone', 'size', 'biased', 'variant', 'surrogates.', 'white', 'mood.', 'anxiety,', 'transformed', 'several', 'age', 'We', 'longitudinally', 'million', '5', 'epidemics,', 'included', 'sensitivity', 'cell', 'characteristics', 'Coefficient', 'Posttraumatic', 'Here,', 'clinical,', 'estimate', 'off', 'monoclonal', 'limits', 'clinical', 'States', 'deter', 'learning', 'using', 'speech', 'in-', 'Physicians', 'defining', 'selection,', 'combined', 'optimal', 'simplicity.', 'comfort', 'beyond', '(PTSD),', 'analysis.', 'scared', 'having', 'Stress', 'February', 'worldwide', 'used', 'at', 'cost-effective', 'families', 'meta-analyses', 'deaths', 'form', 'association', 'insomnia,', 'level', '2020', 'six', 'recordings,', 'physicians.', 'classifier,', 'low', 'Voice', 'objective', 'discriminated', 'syndrome', 'prior', 'CXR,', 'machine', 'labs,', 'suffer', 'might', 'make', 'parallel,', 'PTS', 'Findings', 'examined', 'most', 'radiological,', 'date', 'traditional', 'illness,', 'significant', 'cost.', 'datasets,', 'needed', 'forced-cough', 'Explainable', 'regression', 'often', 'Risk', 'augment', 'pre-screening', 'Although', 'receptor.', 'posttraumatic', 'monitor', 'SARS-CoV-2', 'serum', 'Pandemic.\n\nWe', 'during', '(RF)', 'tool.', 'height', 'physicians', 'system', 'glucocorticoids', '3', '19%', 'analyzed', 'advise', 'thoughts', 'racial/ethnic', 'built', 'Forest', 'challenging.', 'scheme', 'due', 'campus', 'individuals,', 'whose', 'cross-sectional', 'time', 'inputted', 'life-saving,', 'behavioral', 'resulted', 'Network', 'slightly', 'dataset.', 'aimed', "Alzheimer's,", 'Frequency', 'subjects', 'frequency', 'not', 'combines', 'many', 'layer', 'dynamics', 'obesity,', 'non-pharmaceutical', 'cause', 'which', 'assessed', 'Recordings.\n\nWe', 'extracted,', 'taking', 'particularly', 'increased', 'SubPTSD.', 'practice', 'Methods:', '(CNN)', 'strategies', 'outputting', '(CXR),', 'variable', 'our', 'pediatric', 'subjects.', 'predict', 'ones,', 'that', 'self-isolation,', '0.05).', 'academic', 'Intelligence.', 'required.', 'Convolutional', 'pre-screen', 'made', 'accuracy', 'can', 'superspreading,', 'have', 'zero', 'of', 'feature', 'fewer', 'epidemic', 'without.', 'symptomatic', 'only', 'variables', 'enhance', 'Critical', 'units.', 'robust', 'begun', 'throughout', 'system,', 'leading', 'especially', 'abnormalities', 'experiences', 'those', 'targeted', 'improves', 'computerized', 'dampening', 'appealing', 'disease', 'more', 'processing', '(NPIs)', 'Johns', 'been', 'Lab', 'Our', '34', 'Mental', '(data', 'labs', 'as', '120', 'working', 'comorbidities', 'hypothesized', 'infections', 'old', 'AI', '1064', 'Only', 'Artificial', 'stochastic', 'their', 'difficult', 'persons', 'spread,', 'point', 'virus', 'training', 'emergency', 'Intelligence', 'survival', 'website', 'laboratory', 'clinicians', 'symptom-based', 'be', '(August', 'cough', 'means', '2019', '2020,', 'control', 'population.', 'up', 'proinflammatory', '(SubPTSD)', 'reported', 'importance', '(PTSD)', 'cognition', 'trials', 'hypertension)', 'Patient', 'tree,', '(p', 'busy', 'month', '2', 'resurgence.', 'online', 'broad', 'selected', 'veterans.', 'expressing'}
numOfWordsFile1 = dict.fromkeys(uniqueWords, 0)
numOfWordsFile1 = dict.fromkeys(uniqueWordsFile, 0)
for word in bagOfWordsFile1:
    numOfWordsFile1[word] += 1

numOfWordsFile2 = dict.fromkeys(uniqueWordsFile, 0)
for word in bagOfWordsFile2:
    numOfWordsFile2[word] += 1

numOfWordsFile3 = dict.fromkeys(uniqueWordsFile, 0)
for word in bagOfWordsFile3:
    numOfWordsFile3[word] += 1

numOfWordsFile4 = dict.fromkeys(uniqueWordsFile, 0)
for word in bagOfWordsFile4:
    numOfWordsFile4[word] += 1

numOfWordsFile5 = dict.fromkeys(uniqueWordsFile, 0)
for word in bagOfWordsFile5:
    numOfWordsFile5[word] += 1

numOfWordsFile6 = dict.fromkeys(uniqueWordsFile, 0)
for word in bagOfWordsFile6:
    numOfWordsFile6[word] += 1

print(numOfWordsFile1)
{'': 0, 'build': 0, 'NPIs': 0, 'multiple': 0, 'by': 0, 'CI,': 0, 'the': 6, 'balanced': 0, 'prevalence': 0, 'patients': 0, 'derived': 0, 'largest': 0, 'diabetes,': 0, 'over': 2, 'group': 0, '294': 0, '1,230': 1, 'delta': 0, 'Neural': 0, 'veterans': 3, 'hyperinflammatory': 0, 'features': 0, 'symptoms': 4, '(February': 1, 'depression,': 1, 'prediction,': 0, 'United': 1, 'regarding': 0, "ResNet50's": 0, 'surveillance': 0, 'October': 0, 'tested': 0, 'outpatient': 0, 'US': 0, 'critical': 0, 'are': 0, 'elevated': 0, 'among': 2, 'pneumonia.': 0, 'were': 0, 'IL-6': 0, 'disorders': 1, 'criteria': 0, 'pipeline': 0, 'outbreaks': 0, 'real-time,': 0, 'assessing': 0, 'less': 1, 'acute': 0, 'rapid': 0, 'and': 5, 'Learning': 0, 'stress': 1, 'SARS-CoV-2,': 0, 'The': 0, 'tracing.': 0, 'could': 0, 'pre-existing': 0, 'remaining': 0, 'environment.': 0, 'university': 0, 'feelings': 0, 'reduce': 0, 'Mel': 0, 'departments': 0, 'branching': 0, 'larger': 0, 'greater': 2, 'tracing,': 0, 'men': 1, 'Diagnosis': 0, 'chest': 0, 'universities': 0, 'Association': 0, 'environment.\n\nThe': 0, 'collection': 0, 'transmission': 0, 'from': 0, 'November': 1, 'subthreshold': 0, 'Disease': 0, 'helpless,': 0, 'between': 0, 'trained': 0, 'AY2021-2022.': 0, 'previously': 0, 'assess': 0, 'quitting': 0, 'signalling': 0, 'contact': 0, '(IL)-6': 0, 'biomarker': 0, 'simple': 0, 'Since': 0, 'presenting': 0, 'a': 0, 'Pediatric': 0, 'COVID-19,': 0, 'intensive': 0, 'year': 1, 'blockade': 0, 'cytokines': 0, 'therapeutic': 0, 'then': 0, 'PTS,': 0, 'therapy': 0, 'Departments.\n\nBetween': 0, 'asymptomatics,': 0, 'Cepstral': 0, '(41%;': 0, 'in': 1, 'measured': 0, 'has': 0, 'depending': 0, 'concentrations': 0, 'At': 0, 'Cough': 0, 'finally': 0, 'high': 0, 'conflicting': 0, 'binary': 0, 'leverages': 0, 'proportion': 0, 'mental': 2, '(PTS)': 0, 'architecture': 0, 'fear': 0, 'Using': 0, 'pandemic': 0, 'infected': 0, 'Coronavirus': 0, 'feeling': 0, 'found': 0, 'to': 4, 'Prediction': 0, 'radiographs': 0, '2021).': 1, 'RF': 0, 'halt': 0, 'factors': 0, 'framework': 0, '5,320': 0, 'steep': 1, 'Boruta': 0, 'MIT': 0, 'offer': 0, 'greatly': 0, 'resulting': 0, 'alcohol': 1, 'CNN-based': 0, 'one': 1, 'increases': 1, 'yielded': 0, 'we': 0, 'experiences.': 0, 'into': 0, 'explainable': 0, 'presymptomatic': 0, 'suggest': 0, 'dataset': 0, 'health': 3, '35-47%).': 0, 'testing.': 0, 'data': 0, 'dying,': 0, 'asymptomatic': 0, 'Women': 1, 'noted': 0, 'who': 0, 'improving': 0, 'saliency': 0, 'isolation': 0, 'pruned': 0, 'recordings': 0, 'with': 2, 'PTSD': 0, 'use': 1, '(eg,': 0, 'characteristic': 0, 'rules': 0, 'Experiences.\n\nPosttraumatic': 0, 'presence': 0, 'Machine': 0, 'Open': 0, 'important': 0, 'As': 0, 'University).': 0, 'non-invasively,': 0, 'risk': 0, 'quick': 0, 'additional': 0, 'need': 1, 'patient': 0, 'Assessment': 0, 'loved': 0, 'people': 0, 'architecture.': 0, 'validated': 0, 'Hopkins': 0, '(AY);': 0, '95%': 0, 'or': 0, 'learn': 0, 'healthy,': 0, 'acoustic': 0, 'cross-validation': 0, 'Namong': 0, 'reliable': 0, 'interventions': 0, 'consequence,': 0, 'secondarily': 0, 'infecting': 0, 'accurately': 0, 'January': 0, 'may': 0, 'coronavirus': 0, 'Care': 0, 'fears': 0, 'than': 0, 'personalized': 0, 'UC': 0, 'achieve': 0, 'significantly': 0, 'created': 0, 'compared': 2, 'pre-pandemic': 2, 'Poisson': 0, 'hospitalisation': 0, 'Who,': 0, 'trajectories': 1, 'States.': 0, 'is': 0, 'Among': 0, '2020-2021': 0, 'but,': 0, 'through': 1, 'process': 0, 'relevant': 0, 'control:': 0, 'Berkeley': 0, 'train': 0, 'results,': 0, 'anxiety': 1, 'negative': 0, 'associative': 0, 'agent': 0, 'continue': 0, 'pre-trained': 0, 'hyperarousal': 0, 'developed': 0, '(opensigma.mit.edu)': 0, 'immunosuppression': 0, 'isolation,': 0, 'but': 1, 'To': 0, 'describe': 0, 'admitted': 0, 'testing': 0, '20%': 0, 'produce': 0, 'discrimination': 0, 'associated': 0, 'continued': 1, 'symptom': 1, 'support': 0, 'COVID-19.\n\nThe': 0, 'Early': 0, '81%': 0, 'approaches': 0, '2020)': 1, 'minority': 1, 'Emergency': 0, 'explored': 0, 'respiratory': 0, 'provide': 0, 'Optimizing': 0, 'essentially': 0, 'simplified,': 0, 'extractors': 0, 'affected': 0, 'its': 0, 'outbreak': 1, 'what,': 0, 'models': 0, 'predominant': 0, 'American': 2, 'Veterans': 1, '(SARS-CoV-2)': 0, 'Checklist-': 0, 'study': 0, 'efforts': 1, 'care': 1, 'infected,': 0, 'May': 0, 'recording': 0, 'including': 0, 'map': 0, 'based': 0, 'ongoing,': 0, 'COVID-19': 2, 'Prevalence': 0, 'audio': 0, 'being': 0, '4256': 0, 'risk.': 0, 'subjects,': 0, 'Demographic': 0, 'interleukin': 0, 'decision': 0, 'on': 0, 'disorder': 1, 'had': 0, 'extracting': 0, 'April': 0, 'diagnostic.': 0, '10-fold': 0, 'young,': 0, 'primarily': 0, 'survey': 0, 'was': 0, 'Transfer': 0, 'individual': 0, 'positive': 0, 'model': 0, 'antibodies': 0, 'Random': 0, 'rising': 0, 'COVID-19.': 0, 'whom': 0, 'an': 0, 'when:effective': 0, 'causative': 0, 'benefit': 0, '<': 0, 'next': 1, 'for': 1, 'pandemic,': 0, 'events': 0, 'successfully': 0, 'severe': 0, 'cannabis': 1, 'some': 0, 'phone': 0, 'size': 0, 'biased': 0, 'variant': 0, 'surrogates.': 0, 'white': 1, 'mood.': 0, 'anxiety,': 0, 'transformed': 0, 'several': 0, 'age': 0, 'We': 0, 'longitudinally': 0, 'million': 0, '5': 0, 'epidemics,': 0, 'included': 0, 'sensitivity': 0, 'cell': 0, 'characteristics': 0, 'Coefficient': 0, 'Posttraumatic': 0, 'Here,': 0, 'clinical,': 0, 'estimate': 0, 'off': 0, 'monoclonal': 0, 'limits': 0, 'clinical': 0, 'States': 1, 'deter': 0, 'learning': 0, 'using': 0, 'speech': 0, 'in-': 0, 'Physicians': 0, 'defining': 0, 'selection,': 0, 'combined': 0, 'optimal': 0, 'simplicity.': 0, 'comfort': 0, 'beyond': 0, '(PTSD),': 1, 'analysis.': 0, 'scared': 0, 'having': 0, 'Stress': 0, 'February': 1, 'worldwide': 0, 'used': 0, 'at': 0, 'cost-effective': 0, 'families': 0, 'meta-analyses': 0, 'deaths': 0, 'form': 0, 'association': 0, 'insomnia,': 0, 'level': 0, '2020': 0, 'six': 0, 'recordings,': 0, 'physicians.': 0, 'classifier,': 0, 'low': 0, 'Voice': 0, 'objective': 0, 'discriminated': 0, 'syndrome': 0, 'prior': 1, 'CXR,': 0, 'machine': 0, 'labs,': 0, 'suffer': 0, 'might': 0, 'make': 0, 'parallel,': 0, 'PTS': 0, 'Findings': 1, 'examined': 1, 'most': 0, 'radiological,': 0, 'date': 0, 'traditional': 0, 'illness,': 0, 'significant': 0, 'cost.': 0, 'datasets,': 0, 'needed': 0, 'forced-cough': 0, 'Explainable': 0, 'regression': 0, 'often': 0, 'Risk': 0, 'augment': 0, 'pre-screening': 0, 'Although': 0, 'receptor.': 0, 'posttraumatic': 1, 'monitor': 0, 'SARS-CoV-2': 0, 'serum': 0, 'Pandemic.\n\nWe': 1, 'during': 1, '(RF)': 0, 'tool.': 0, 'height': 0, 'physicians': 0, 'system': 0, 'glucocorticoids': 0, '3': 0, '19%': 0, 'analyzed': 0, 'advise': 0, 'thoughts': 0, 'racial/ethnic': 1, 'built': 0, 'Forest': 0, 'challenging.': 0, 'scheme': 0, 'due': 0, 'campus': 0, 'individuals,': 0, 'whose': 0, 'cross-sectional': 0, 'time': 2, 'inputted': 0, 'life-saving,': 0, 'behavioral': 0, 'resulted': 0, 'Network': 0, 'slightly': 1, 'dataset.': 0, 'aimed': 0, "Alzheimer's,": 0, 'Frequency': 0, 'subjects': 0, 'frequency': 0, 'not': 0, 'combines': 0, 'many': 0, 'layer': 0, 'dynamics': 0, 'obesity,': 0, 'non-pharmaceutical': 0, 'cause': 0, 'which': 0, 'assessed': 1, 'Recordings.\n\nWe': 0, 'extracted,': 0, 'taking': 0, 'particularly': 0, 'increased': 1, 'SubPTSD.': 0, 'practice': 0, 'Methods:': 0, '(CNN)': 0, 'strategies': 0, 'outputting': 0, '(CXR),': 0, 'variable': 0, 'our': 0, 'pediatric': 0, 'subjects.': 0, 'predict': 0, 'ones,': 0, 'that': 0, 'self-isolation,': 0, '0.05).': 0, 'academic': 0, 'Intelligence.': 0, 'required.': 0, 'Convolutional': 0, 'pre-screen': 0, 'made': 0, 'accuracy': 0, 'can': 0, 'superspreading,': 0, 'have': 0, 'zero': 0, 'of': 1, 'feature': 0, 'fewer': 0, 'epidemic': 0, 'without.': 1, 'symptomatic': 0, 'only': 0, 'variables': 0, 'enhance': 0, 'Critical': 0, 'units.': 0, 'robust': 0, 'begun': 0, 'throughout': 0, 'system,': 0, 'leading': 0, 'especially': 0, 'abnormalities': 0, 'experiences': 0, 'those': 2, 'targeted': 0, 'improves': 0, 'computerized': 0, 'dampening': 0, 'appealing': 0, 'disease': 0, 'more': 0, 'processing': 0, '(NPIs)': 0, 'Johns': 0, 'been': 0, 'Lab': 0, 'Our': 0, '34': 0, 'Mental': 1, '(data': 0, 'labs': 0, 'as': 0, '120': 0, 'working': 0, 'comorbidities': 0, 'hypothesized': 0, 'infections': 0, 'old': 0, 'AI': 0, '1064': 0, 'Only': 0, 'Artificial': 0, 'stochastic': 0, 'their': 0, 'difficult': 0, 'persons': 0, 'spread,': 0, 'point': 1, 'virus': 0, 'training': 0, 'emergency': 0, 'Intelligence': 0, 'survival': 0, 'website': 0, 'laboratory': 0, 'clinicians': 0, 'symptom-based': 0, 'be': 0, '(August': 1, 'cough': 0, 'means': 0, '2019': 0, '2020,': 2, 'control': 0, 'population.': 0, 'up': 0, 'proinflammatory': 0, '(SubPTSD)': 0, 'reported': 2, 'importance': 0, '(PTSD)': 0, 'cognition': 0, 'trials': 0, 'hypertension)': 0, 'Patient': 0, 'tree,': 0, '(p': 0, 'busy': 0, 'month': 1, '2': 0, 'resurgence.': 0, 'online': 1, 'broad': 0, 'selected': 0, 'veterans.': 2, 'expressing': 0}
print(numOfWordsFile2)

print(numOfWordsFile3)

print(numOfWordsFile4)

print(numOfWordsFile5)

print(numOfWordsFile6)

from nltk.corpus import stopwords
stopwords.words('english')
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
def computeTF(wordDict, bagOfWordsFile):
    tfDict = []
    bagOfWordsFileCount = len(bagOfWordsFile)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsFileCount)
    return tfDict

tf1 = coumputeTF(numOfWordsFile1, bagOfWordsFile1)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    tf1 = coumputeTF(numOfWordsFile1, bagOfWordsFile1)
NameError: name 'coumputeTF' is not defined. Did you mean: 'computeTF'?
tf1 = computeTF(numOfWordsFile1, bagOfWordsFile1)
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    tf1 = computeTF(numOfWordsFile1, bagOfWordsFile1)
  File "<pyshell#163>", line 5, in computeTF
    tfDict[word] = count / float(bagOfWordsFileCount)
TypeError: list indices must be integers or slices, not str
tfa = computeTF(numOfWordsFile1, bagOfWordsFile1)
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    tfa = computeTF(numOfWordsFile1, bagOfWordsFile1)
  File "<pyshell#163>", line 5, in computeTF
    tfDict[word] = count / float(bagOfWordsFileCount)
TypeError: list indices must be integers or slices, not str
def computeTF(wordDict, bagOfWordsFile):
    tfDict = {}
    bagOfWordsFileCount = len(bagOfWordsFile)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsFileCount)
    return tfDict

tf1 = computeTF(numOfWordsFile1, bagOfWordsFile1)
tf2 = computeTF(numOfWordsFile2, bagOfWordsFile2)
tf3 = computeTF(numOfWordsFile3, bagOfWordsFile3)
tf4 = computeTF(numOfWordsFile4, bagOfWordsFile4)
tf5 = computeTF(numOfWordsFile5, bagOfWordsFile5)
tf6 = computeTF(numOfWordsFile6, bagOfWordsFile6)
def computeIDF(documents):
    import math
    N = len(documents)

    
def computeIDF(documents):
    import math
    N = len(documents)
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

   
def computeIDF(documents):
    import math
    N = len(documents)
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

idfs = computeIDF([numOfWordsFile1, numOfWordsFile2, numOfWordsFile3, numOfWordsFile4, numOfWordsFile5, numOfWordsFile6])
def computeTFIDF(tfBagOfWordsFile, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidf1 = computeTFIDF(tf1, idfs)
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    tfidf1 = computeTFIDF(tf1, idfs)
  File "<pyshell#204>", line 3, in computeTFIDF
    for word, val in tfBagOfWords.items():
NameError: name 'tfBagOfWords' is not defined. Did you mean: 'tfBagOfWordsFile'?
def computeTFIDF(tfBagOfWordsFile, idfs):
    tfidf = {}
    for word, val in tfBagOfWordsFile.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidf1 = computeTFIDF(tf1, idfs)
tfidf2 = computeTFIDF(tf2, idfs)
tfidf3 = computeTFIDF(tf3, idfs)
tfidf4 = computeTFIDF(tf4, idfs)
tfidf5 = computeTFIDF(tf5, idfs)
tfidf6 = computeTFIDF(tf6, idfs)
df = pd.DataFrame([tfidf1, tfidf2, tfidf3, tfidf4, tfidf5, tfidf6])
print(df)
                build      NPIs  ...  selected  veterans.  expressing
0  0.000000  0.000000  0.000000  ...  0.000000   0.032876    0.000000
1  0.002278  0.000000  0.010066  ...  0.000000   0.000000    0.000000
2  0.003588  0.000000  0.000000  ...  0.000000   0.000000    0.007928
3  0.000000  0.000000  0.000000  ...  0.000000   0.000000    0.000000
4  0.002058  0.000000  0.000000  ...  0.000000   0.000000    0.000000
5  0.001860  0.008219  0.000000  ...  0.008219   0.000000    0.000000

[6 rows x 615 columns]
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([text1, text2, text3, text4, text5, text6])
feature_names = vectorizer.get_feature_names()

Warning (from warnings module):
  File "C:\Users\Faisal\AppData\Roaming\Python\Python310\site-packages\sklearn\utils\deprecation.py", line 87
    warnings.warn(msg, category=FutureWarning)
FutureWarning: Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
feature_names = vectorizer.get_feature_names_out()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)
df2 = pd.DataFrame(denselist, columns=feature_names)
print(df2)
         05        10      1064  ...   yielded     young      zero
0  0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.000000
1  0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.000000
2  0.046057  0.000000  0.000000  ...  0.000000  0.000000  0.000000
3  0.000000  0.000000  0.000000  ...  0.067538  0.067538  0.000000
4  0.000000  0.000000  0.059085  ...  0.000000  0.000000  0.059085
5  0.000000  0.061794  0.000000  ...  0.000000  0.000000  0.000000

[6 rows x 535 columns]
import pandas
df2 = pd.DataFrame(denselist, columns=feature_names)
print(df3)
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    print(df3)
NameError: name 'df3' is not defined. Did you mean: 'tf3'?
print(df2)
         05        10      1064  ...   yielded     young      zero
0  0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.000000
1  0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.000000
2  0.046057  0.000000  0.000000  ...  0.000000  0.000000  0.000000
3  0.000000  0.000000  0.000000  ...  0.067538  0.067538  0.000000
4  0.000000  0.000000  0.059085  ...  0.000000  0.000000  0.059085
5  0.000000  0.061794  0.000000  ...  0.000000  0.000000  0.000000

[6 rows x 535 columns]
