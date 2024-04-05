import psycopg2

# CONNECT TO DATBASE
conn = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="password",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()

# Define the CREATE TABLE query
create_table_query = '''
CREATE TABLE "episodes" (
  "EpisodeID" varchar PRIMARY KEY,
  "Title" varchar,
  "AirDate" date,
  "Notes" varchar
);

CREATE TABLE "colors" (
  "ColorID" varchar PRIMARY KEY,
  "ColorName" varchar,
  "ColorHex" varchar
);

CREATE TABLE "episodeColors" (
  "EpisodeID" varchar,
  "ColorID" varchar
);

CREATE TABLE "subjects" (
  "SubjectID" varchar PRIMARY KEY,
  "SubjectType" varchar
);

CREATE TABLE "episodeSubjects" (
  "EpisodeID" varchar,
  "SubjectID" varchar
);

ALTER TABLE "episodeColors" ADD FOREIGN KEY ("EpisodeID") REFERENCES "episodes" ("EpisodeID");

ALTER TABLE "episodeSubjects" ADD FOREIGN KEY ("EpisodeID") REFERENCES "episodes" ("EpisodeID");

ALTER TABLE "episodeSubjects" ADD FOREIGN KEY ("SubjectID") REFERENCES "subjects" ("SubjectID");

ALTER TABLE "episodeColors" ADD FOREIGN KEY ("ColorID") REFERENCES "colors" ("ColorID");

'''
cur.execute(create_table_query)

# Commit the transaction
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
