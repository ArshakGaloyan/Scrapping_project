use epl;
-- ALTER TABLE `season2000_2001`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2001_2002`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2002_2003`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2003_2004`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2004_2005`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2005_2006`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2006_2007`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2007_2008`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2008_2009`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2009_2010`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2010_2011`
-- --, ADD COLUMN `Position` INT;,
-- ALTER TABLE `season2011_2012`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2012_2013`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2013_2014`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2014_2015`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2015_2016`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2016_2017`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2017_2018`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2018_2019`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2020_2021`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2021_2022`
-- ADD COLUMN `Position` INT;
-- ALTER TABLE `season2022_2023`
-- ADD COLUMN `Position` INT;
-- DELETE FROM season2000_2001 WHERE Position = 1;
-- DELETE FROM season2000_2001 WHERE Position = 2;
-- DELETE FROM season2000_2001 WHERE Position = 3;
-- DELETE FROM season2000_2001 WHERE Position = 4;
-- DELETE FROM season2000_2001 WHERE Position = 5;
-- DELETE FROM season2000_2001 WHERE Position = 6;
-- DELETE FROM season2000_2001 WHERE Position = 7;
-- DELETE FROM season2000_2001 WHERE Position = 8;
-- DELETE FROM season2000_2001 WHERE Position = 9;
-- DELETE FROM season2000_2001 WHERE Position = 10;
-- DELETE FROM season2000_2001 WHERE Position = 12;
-- DELETE FROM season2000_2001 WHERE Position = 13;
-- DELETE FROM season2000_2001 WHERE Position = 14;
-- DELETE FROM season2000_2001 WHERE Position = 15;
-- DELETE FROM season2000_2001 WHERE Position = 16;
-- DELETE FROM season2000_2001 WHERE Position = 17;
-- DELETE FROM season2000_2001 WHERE Position = 18;
-- DELETE FROM season2000_2001 WHERE Position = 19;
-- DELETE FROM season2000_2001 WHERE Position = 20;
-- DELETE FROM season2000_2001 WHERE Position = 11;

-- SET @row_number = 0;

-- -- Обновляем значения в столбце `Position` в зависимости от NULL
-- UPDATE season2000_2001
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- Устанавливаем переменную для начального значения
-- SET @row_number = 0;

-- Обновляем значения в столбце `Position` в зависимости от NULL
-- UPDATE season2000_2001
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2001_2002
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2002_2003
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2003_2004
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2004_2005
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2005_2006
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2006_2007
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2007_2008
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2008_2009
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2009_2010
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2010_2011
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2011_2012
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2012_2013
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;


-- UPDATE season2013_2014
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2014_2015
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2016_2017
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2017_2018
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2018_2019
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2019_2020
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2020_2021
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;

-- UPDATE season2021_2022
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL;
-- SET SQL_SAFE_UPDATES = 0;
-- UPDATE season2011_2012
-- SET position = NULL;
-- SET @row_number = 0;

-- UPDATE season2011_2012
-- SET Position = (@row_number := @row_number + 1)
-- WHERE Position IS NULL


















