CREATE TABLE public.overdue (
  "ID" BIGINT STORAGE PLAIN GENERATED ALWAYS AS IDENTITY NOT NULL,
  "SUBJ" VARCHAR(250) STORAGE PLAIN NOT NULL,
  "DOZ" INTEGER STORAGE PLAIN NOT NULL,
  "DAYS" INTEGER STORAGE PLAIN NOT NULL,
  CONSTRAINT "overdue_ID_key" UNIQUE("ID")
) ;

ALTER TABLE public.overdue
  ALTER COLUMN "ID" SET STATISTICS 0;

CREATE INDEX overdue_subj_idx ON public.overdue
  USING btree ("SUBJ" COLLATE pg_catalog."default");

ALTER TABLE public.overdue
  OWNER TO postgres;

ALTER TABLE public.overdue
  ALTER COLUMN "SUBJ" SET STORAGE PLAIN;