-- Ideally you would also parameterize the database name, etc. 
-- but I'm lazy so hardcoding it is

-- lat, lon parameterized for obvious reasons 
-- (this will be filled in by python script)


SELECT state_name
FROM

-- this subquery just gets a list of states and a true/flase if point in a state
(
SELECT STATES.name as state_name, ST_WITHIN(PNT.geom, STATES.geom) as point_in_state

FROM
-- *** SOURCES - states data, point input *** --

-- states to check against
(SELECT name, geom FROM public.cb_2018_us_state_500k) STATES

CROSS JOIN

-- input of lat and lon
(SELECT ST_SetSRID(ST_MakePoint(${LONGITUDE}, ${LATITUDE}), 4326) as geom) PNT

-- *** END SOURCES *** --
) state_check

WHERE point_in_state = true