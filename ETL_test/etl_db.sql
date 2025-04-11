-- SQL Manager for PostgreSQL 6.6.0.58686
-- ---------------------------------------
-- Хост         : 192.168.2.74:49172
-- База данных  : etl_db
-- Версия       : PostgreSQL 17.4 (Debian 17.4-1.pgdg120+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3360 (class 1262 OID 16384)
-- Name: etl; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE etl_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'ru_RU.UTF-8';


ALTER DATABASE etl_db OWNER TO postgres;

\connect etl


SET check_function_bodies = false;
--
-- Structure for table overdue (OID = 16391) : 
--
SET search_path = public, pg_catalog;
CREATE TABLE public.overdue (
    "ID" bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
    "SUBJ" varchar(250) NOT NULL,
    "DOZ" integer NOT NULL,
    "DAYS" integer NOT NULL
)
WITH (oids = false);
ALTER TABLE ONLY public.overdue ALTER COLUMN "ID" SET STATISTICS 0;
ALTER TABLE ONLY public.overdue ALTER COLUMN "SUBJ" SET STATISTICS 0;
ALTER TABLE ONLY public.overdue ALTER COLUMN "DOZ" SET STATISTICS 0;
ALTER TABLE ONLY public.overdue ALTER COLUMN "DAYS" SET STATISTICS 0;
--
-- Definition for index overdue_subj_idx (OID = 16396) : 
--
CREATE INDEX overdue_subj_idx ON public.overdue USING btree ("SUBJ");
--
-- Definition for index overdue_ID_key (OID = 16394) : 
--
ALTER TABLE ONLY public.overdue
    ADD CONSTRAINT "overdue_ID_key"
    UNIQUE ("ID");
--
-- Comments
--
COMMENT ON SCHEMA public IS 'standard public schema';
