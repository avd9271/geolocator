SELECT *, ST_WITHIN(PNT.geom, NC.geom) as is_point_in_NC FROM

-- NC geom
-- srid 4326
(SELECT '500 k srid4326' as source_name, geom FROM public.cb_2018_us_state_500k where name = 'North Carolina') NC

CROSS JOIN

-- point geom
-- srid 4326
-- input is long, lat
(

-- long -78.623877
-- lat 35.738466
SELECT 
'NC point' as source_name, 
ST_SetSRID(ST_MakePoint(-78.623877, 35.738466), 4326) as geom

UNION ALL
	
-- long -79.915102
-- lat 34.571673
SELECT
'Non NC point (SC BORDER)' as source_name,
ST_SetSRID(ST_MakePoint(-79.915102, 34.571673), 4326) as geom

) PNT
