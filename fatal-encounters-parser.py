import pandas

df = pandas.read_csv('fatal_encounters.csv')

# Print the shape of the dataframe before parsing
print(df.shape) 

# add unarmed column to all rows
df["unarmed"] = None

# First filter out those rows which 
# does not contain any data 
df = df.dropna(how = 'all') 

#Subject's race with imputations
# df = df[df["Subject's race with imputations"].str.contains('African-American') | df["Subject's race with imputations"].str.contains('Black')] 

# if row titled Subject's race contains African-American or Black
df = df[df["Subject's race"].str.contains('African-American') | df["Subject's race"].str.contains('Black')] 

# if row titled A brief description of the circumstances surrounding the death contains unarmed, not holding, or no weapon 
# unarmed column equals True 
df["unarmed"][df["A brief description of the circumstances surrounding the death"].str.contains('unarmed') | df["A brief description of the circumstances surrounding the death"].str.contains('not holding') | df["A brief description of the circumstances surrounding the death"].str.contains('no weapon')] = True
# df = df[df["A brief description of the circumstances surrounding the death"].str.contains('unarmed') | df["A brief description of the circumstances surrounding the death"].str.contains('not holding') | df["A brief description of the circumstances surrounding the death"].str.contains('no weapon')]

# Print the new dataframe 
print(df)
  
# Print the shape of the dataframe after parsing
print(df.shape) 

df.to_csv('parsed_fatal_encounters.csv', index=False)
