CREATE TABLE "episodes" (
  "EpisodeID" SERIAL PRIMARY KEY,
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
