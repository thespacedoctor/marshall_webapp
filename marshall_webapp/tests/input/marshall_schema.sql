-- MySQL dump 10.17  Distrib 10.3.25-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: 10.131.21.162    Database: marshall
-- ------------------------------------------------------
-- Server version	10.4.17-MariaDB-1:10.4.17+maria~focal-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary table structure for view `_subview_object_akas`
--

DROP TABLE IF EXISTS `_subview_object_akas`;
/*!50001 DROP VIEW IF EXISTS `_subview_object_akas`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `_subview_object_akas` (
  `transientBucketId` tinyint NOT NULL,
  `primaryKeyId` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `surveyObjectUrl` tinyint NOT NULL,
  `referenceImageUrl` tinyint NOT NULL,
  `targetImageUrl` tinyint NOT NULL,
  `subtractedImageUrl` tinyint NOT NULL,
  `tripletImageUrl` tinyint NOT NULL,
  `finderImageUrl` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `atel_coordinates`
--

DROP TABLE IF EXISTS `atel_coordinates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `atel_coordinates` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT,
  `atelNumber` int(11) NOT NULL,
  `raDeg` double NOT NULL,
  `decDeg` double NOT NULL,
  `crossMatchDate` datetime DEFAULT NULL,
  `singleClassification` varchar(45) DEFAULT NULL,
  `supernovaTag` int(11) DEFAULT NULL,
  `ingested` int(11) DEFAULT 0,
  `atelName` varchar(45) NOT NULL,
  `atelUrl` varchar(200) NOT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `survey` varchar(45) NOT NULL,
  `titleToComment` tinyint(4) NOT NULL DEFAULT 0,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `updated` tinyint(1) DEFAULT 0,
  `dateLastModified` datetime DEFAULT current_timestamp(),
  `dateCreated` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `atelnumber_ra_dec` (`atelNumber`,`raDeg`,`decDeg`),
  KEY `ra_deg` (`raDeg`,`decDeg`),
  KEY `atelNumber` (`atelNumber`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `atel_fullcontent`
--

DROP TABLE IF EXISTS `atel_fullcontent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `atel_fullcontent` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `atelNumber` int(11) DEFAULT NULL,
  `authors` mediumtext DEFAULT NULL,
  `backRefList` varchar(450) DEFAULT NULL,
  `dateCreated` datetime DEFAULT NULL,
  `dateLastModified` datetime DEFAULT NULL,
  `dateLastRead` datetime DEFAULT NULL,
  `email` varchar(450) DEFAULT NULL,
  `refList` varchar(450) DEFAULT NULL,
  `tags` varchar(450) DEFAULT NULL,
  `title` varchar(450) DEFAULT NULL,
  `userText` mediumtext DEFAULT NULL,
  `datePublished` datetime NOT NULL,
  `atelType` varchar(500) DEFAULT NULL,
  `dateParsed` datetime DEFAULT NULL COMMENT 'The date the ATel text was parsed for names and coordinates',
  `updated` tinyint(4) DEFAULT 0,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `atelnumber` (`atelNumber`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `atel_names`
--

DROP TABLE IF EXISTS `atel_names`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `atel_names` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT,
  `atelNumber` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `crossMatchDate` datetime DEFAULT NULL,
  `singleClassification` varchar(45) DEFAULT NULL,
  `supernovaTag` int(11) DEFAULT NULL,
  `ingested` int(11) DEFAULT 0,
  `atelName` varchar(45) NOT NULL,
  `atelUrl` varchar(200) NOT NULL,
  `survey` varchar(45) NOT NULL,
  `titleToComment` tinyint(4) NOT NULL DEFAULT 0,
  `summaryRow` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `atelnumber_name` (`atelNumber`,`name`),
  KEY `atelNumber` (`atelNumber`),
  KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_asassn_sne`
--

DROP TABLE IF EXISTS `fs_asassn_sne`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_asassn_sne` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `Classification_Age` varchar(100) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `Disc_Age` varchar(100) DEFAULT NULL,
  `Galaxy_name` varchar(100) DEFAULT NULL,
  `ID` varchar(100) DEFAULT NULL,
  `No` varchar(100) DEFAULT NULL,
  `Offset` double DEFAULT NULL,
  `RA` double DEFAULT NULL,
  `Redshift` double DEFAULT NULL,
  `Type` varchar(100) DEFAULT NULL,
  `V_abs` double DEFAULT NULL,
  `V_disc` double DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `decl` double DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `surveyUrl` varchar(100) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `id` (`ID`,`Date`),
  UNIQUE KEY `id_date` (`ID`,`Date`),
  KEY `htm16` (`htm16ID`),
  KEY `ra_dec` (`RA`,`decl`),
  KEY `ingested` (`ingested`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_asassn_transients`
--

DROP TABLE IF EXISTS `fs_asassn_transients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_asassn_transients` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `Vmag` double DEFAULT NULL,
  `comment` varchar(700) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `decDeg` double DEFAULT NULL,
  `discDate` datetime DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `specClass` varchar(100) DEFAULT NULL,
  `commentAdded` tinyint(4) NOT NULL DEFAULT 0,
  `surveyUrl` varchar(100) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `name` (`name`),
  KEY `ra_dec` (`decDeg`,`raDeg`),
  KEY `html16` (`htm16ID`),
  KEY `ingested` (`ingested`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_atlas`
--

DROP TABLE IF EXISTS `fs_atlas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_atlas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `candidateID` varchar(20) NOT NULL,
  `ra_deg` double NOT NULL,
  `dec_deg` double NOT NULL,
  `mag` float DEFAULT NULL,
  `magErr` float DEFAULT NULL COMMENT 'Mag error only available in the recurrence data',
  `filter` varchar(10) DEFAULT NULL COMMENT 'Observaton filter',
  `observationMJD` double DEFAULT NULL COMMENT 'Observation date in MJD',
  `discDate` datetime DEFAULT NULL,
  `discMag` float DEFAULT NULL,
  `suggestedType` varchar(50) DEFAULT NULL,
  `catalogType` varchar(50) DEFAULT NULL,
  `hostZ` float DEFAULT NULL,
  `targetImageURL` varchar(512) DEFAULT NULL,
  `refImageURL` varchar(512) DEFAULT NULL,
  `diffImageURL` varchar(512) DEFAULT NULL,
  `objectURL` varchar(512) DEFAULT NULL,
  `summaryRow` tinyint(1) NOT NULL DEFAULT 1 COMMENT 'Summary row flag. 1 = summary row, 0 = recurrence. There should always be one summary row and at least one recurrence.',
  `ingested` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Transient Bucket ingest flag.  Has this data been ingested yet?',
  `htm16ID` bigint(20) unsigned DEFAULT NULL,
  `survey` varchar(45) NOT NULL DEFAULT 'ATLAS',
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `dateLastRead` datetime DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `updated` tinyint(4) DEFAULT 0,
  `cz` double DEFAULT NULL,
  `cx` double DEFAULT NULL,
  `htm20ID` bigint(20) DEFAULT NULL,
  `cy` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_uq_candidateID_observationMJD_mag_filter_summaryRow` (`candidateID`,`observationMJD`,`mag`,`filter`,`summaryRow`),
  UNIQUE KEY `idx_uq_candidateID_discDate` (`candidateID`,`discDate`),
  KEY `idx_candidateID` (`candidateID`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `htm16` (`htm16ID`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`),
  KEY `idx_htm20ID` (`htm20ID`),
  KEY `idx_transientBucketId` (`transientBucketId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_atlas_forced_phot`
--

DROP TABLE IF EXISTS `fs_atlas_forced_phot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_atlas_forced_phot` (
  `primaryId` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `atlas_object_id` bigint(20) unsigned NOT NULL,
  `atlas_designation` varchar(255) NOT NULL,
  `mjd_obs` double NOT NULL,
  `filter` varchar(10) NOT NULL,
  `mag` float NOT NULL,
  `dm` float DEFAULT NULL,
  `snr` float DEFAULT NULL,
  `zp` float DEFAULT NULL,
  `limiting_mag` tinyint(1) NOT NULL,
  `raDeg` double NOT NULL,
  `decDeg` double NOT NULL,
  `ingested` tinyint(4) DEFAULT 0,
  `survey` varchar(45) DEFAULT 'ATLAS FP',
  `htm16ID` bigint(20) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `peakval` float DEFAULT NULL,
  `skyval` float DEFAULT NULL,
  `peakfit` float DEFAULT NULL,
  `dpeak` float DEFAULT NULL,
  `skyfit` float DEFAULT NULL,
  `flux` float DEFAULT NULL,
  `dflux` float DEFAULT NULL,
  `chin` float DEFAULT NULL,
  `major` float DEFAULT NULL,
  `minor` float DEFAULT NULL,
  `snrdet` float DEFAULT NULL,
  `snrlimit` float DEFAULT NULL,
  `wpflx` float DEFAULT NULL,
  `dwpflx` float DEFAULT NULL,
  `texp` float DEFAULT NULL,
  `expname` varchar(45) DEFAULT NULL,
  `apfit` float DEFAULT NULL,
  `fnu` float DEFAULT NULL,
  `marshall_mag` float DEFAULT NULL,
  `marshall_limiting_mag` float DEFAULT NULL,
  `marshall_mag_error` float DEFAULT NULL,
  `fnu_error` float DEFAULT NULL,
  `updated` tinyint(4) DEFAULT 0,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `transientBucketId` bigint(20) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `object_id_mjd` (`atlas_object_id`,`mjd_obs`),
  KEY `atlas_object_id` (`atlas_object_id`),
  KEY `mjd_obs` (`mjd_obs`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`),
  KEY `idx_transientBucketId` (`transientBucketId`),
  KEY `idx_atlas_designation` (`atlas_designation`),
  KEY `idx_dateCreated` (`dateCreated`),
  KEY `idx_transientBucketId_designation` (`atlas_designation`,`transientBucketId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_crts_css`
--

DROP TABLE IF EXISTS `fs_crts_css`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_crts_css` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `circularUrl` varchar(450) DEFAULT NULL,
  `comment` mediumtext DEFAULT NULL,
  `commentIngested` tinyint(4) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `dateLastRead` datetime DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `filter` varchar(450) DEFAULT NULL,
  `finderChartUrl` varchar(644) DEFAULT NULL,
  `finderChartWebpage` varchar(450) DEFAULT NULL,
  `imagesUrl` varchar(450) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `lightcurveUrl` varchar(450) DEFAULT NULL,
  `mag` double DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `observationDate` varchar(450) DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `survey` varchar(450) DEFAULT NULL,
  `surveyObjectUrl` varchar(450) DEFAULT NULL,
  `targetImageUrl` varchar(624) DEFAULT NULL,
  `transientTypePrediction` varchar(450) DEFAULT NULL,
  `uniqueId` bigint(20) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `magErr` double DEFAULT NULL,
  `lastNonDetectionDate` datetime DEFAULT NULL,
  `lastNonDetectionMJD` double DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `observationmjd_name` (`observationMJD`,`name`),
  KEY `name` (`name`),
  KEY `htm16` (`htm16ID`),
  KEY `ra_dec` (`decDeg`,`raDeg`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm10ID`),
  KEY `idx_htm13ID` (`htm13ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_crts_mls`
--

DROP TABLE IF EXISTS `fs_crts_mls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_crts_mls` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `circularUrl` varchar(450) DEFAULT NULL,
  `comment` mediumtext DEFAULT NULL,
  `commentIngested` tinyint(4) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `dateLastRead` datetime DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `filter` varchar(450) DEFAULT NULL,
  `finderChartUrl` varchar(618) DEFAULT NULL,
  `finderChartWebpage` varchar(450) DEFAULT NULL,
  `imagesUrl` varchar(450) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `lightcurveUrl` varchar(450) DEFAULT NULL,
  `mag` double DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `observationDate` varchar(450) DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `survey` varchar(450) DEFAULT NULL,
  `surveyObjectUrl` varchar(450) DEFAULT NULL,
  `targetImageUrl` varchar(614) DEFAULT NULL,
  `transientTypePrediction` varchar(450) DEFAULT NULL,
  `uniqueId` bigint(20) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `magErr` double DEFAULT NULL,
  `lastNonDetectionDate` datetime DEFAULT NULL,
  `lastNonDetectionMJD` double DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `observationmjd_name` (`observationMJD`,`name`),
  KEY `name` (`name`),
  KEY `htm16` (`htm16ID`),
  KEY `ra_dec` (`decDeg`,`raDeg`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm10ID`),
  KEY `idx_htm13ID` (`htm13ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_crts_sss`
--

DROP TABLE IF EXISTS `fs_crts_sss`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_crts_sss` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `circularUrl` varchar(450) DEFAULT NULL,
  `comment` mediumtext DEFAULT NULL,
  `commentIngested` tinyint(4) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `dateLastRead` datetime DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `filter` varchar(450) DEFAULT NULL,
  `finderChartUrl` varchar(618) DEFAULT NULL,
  `finderChartWebpage` varchar(450) DEFAULT NULL,
  `imagesUrl` varchar(450) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `lightcurveUrl` varchar(450) DEFAULT NULL,
  `mag` double DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `observationDate` varchar(450) DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `survey` varchar(450) DEFAULT NULL,
  `surveyObjectUrl` varchar(450) DEFAULT NULL,
  `targetImageUrl` varchar(614) DEFAULT NULL,
  `transientTypePrediction` varchar(450) DEFAULT NULL,
  `uniqueId` bigint(20) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `magErr` double DEFAULT NULL,
  `lastNonDetectionDate` datetime DEFAULT NULL,
  `lastNonDetectionMJD` double DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `observationmjd_name` (`observationMJD`,`name`),
  KEY `name` (`name`),
  KEY `htm16` (`htm16ID`),
  KEY `ra_dec` (`decDeg`,`raDeg`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm10ID`),
  KEY `idx_htm13ID` (`htm13ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_des`
--

DROP TABLE IF EXISTS `fs_des`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_des` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `dateCreated` datetime DEFAULT current_timestamp(),
  `decDeg` double DEFAULT NULL,
  `filter` varchar(100) DEFAULT NULL,
  `lastNonDetectionDate` datetime DEFAULT NULL,
  `lastNonDetectionMJD` double DEFAULT NULL,
  `limitingMag` tinyint(4) DEFAULT NULL,
  `magnitude` double DEFAULT NULL,
  `magnitudeError` double DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `observationDate` datetime DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `signal_to_noise` double DEFAULT NULL,
  `stampUrl` varchar(690) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `survey` varchar(100) DEFAULT NULL,
  `surveyUrl` varchar(100) DEFAULT NULL,
  `transientTypePrediction` varchar(100) DEFAULT NULL,
  `finderImageUrl` varchar(100) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `diffUrl` varchar(684) DEFAULT NULL,
  `refUrl` varchar(684) DEFAULT NULL,
  `tarUrl` varchar(682) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `name_observationmjd` (`name`,`observationMJD`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_gaia`
--

DROP TABLE IF EXISTS `fs_gaia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_gaia` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `candidateID` varchar(100) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dec_deg` double DEFAULT NULL,
  `discDate` varchar(100) DEFAULT NULL,
  `discMag` double DEFAULT NULL,
  `filter` varchar(100) DEFAULT NULL,
  `mag` double DEFAULT NULL,
  `objectURL` varchar(100) DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `ra_deg` double DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `survey` varchar(10) DEFAULT 'Gaia',
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `cz` double DEFAULT NULL,
  `cx` double DEFAULT NULL,
  `htm20ID` bigint(20) DEFAULT NULL,
  `cy` double DEFAULT NULL,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `candidateid_observationmjd` (`candidateID`,`observationMJD`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`),
  KEY `idx_htm20ID` (`htm20ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_master`
--

DROP TABLE IF EXISTS `fs_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_master` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `comment` varchar(700) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `imageUrl` varchar(200) DEFAULT NULL,
  `magnitude` double DEFAULT NULL,
  `masterInt` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `telescope` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `survey` varchar(45) DEFAULT 'master',
  `discoveryMjd` double DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `filter` varchar(45) DEFAULT 'unfiltered',
  `candidateUrl` varchar(100) DEFAULT 'http://observ.pereplet.ru/sn_e.html',
  `ingested` tinyint(4) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `day` varchar(100) DEFAULT NULL,
  `month` varchar(100) DEFAULT NULL,
  `tripletImageUrl` varchar(100) DEFAULT NULL,
  `year` varchar(100) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `name` (`name`),
  KEY `htm16` (`htm16ID`),
  KEY `ra_dec` (`decDeg`,`raDeg`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_ogle`
--

DROP TABLE IF EXISTS `fs_ogle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_ogle` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `dateLastRead` datetime DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `filter` varchar(450) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `lastNonDetectionDate` varchar(450) DEFAULT NULL,
  `lastNonDetectionMJD` double DEFAULT NULL,
  `lightcurveUrl` varchar(614) DEFAULT NULL,
  `mag` double DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `observationDate` varchar(450) DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `referenceFitsUrl` varchar(616) DEFAULT NULL,
  `referenceImageUrl` varchar(616) DEFAULT NULL,
  `subtractedFitsUrl` varchar(634) DEFAULT NULL,
  `subtractedImageUrl` varchar(634) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `survey` varchar(50) DEFAULT NULL,
  `surveyObjectUrl` varchar(450) DEFAULT NULL,
  `targetFitsUrl` varchar(638) DEFAULT NULL,
  `targetImageUrl` varchar(638) DEFAULT NULL,
  `transientTypePrediction` varchar(450) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `seeing` double DEFAULT NULL,
  `background` double DEFAULT NULL,
  `magErr` double DEFAULT NULL,
  `limitingMag` tinyint(4) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `observationmjd_name_survey` (`observationMJD`,`name`,`survey`),
  UNIQUE KEY `observationmjd_name` (`observationMJD`,`name`),
  KEY `name` (`name`),
  KEY `htm16` (`htm16ID`),
  KEY `ra_dec` (`decDeg`,`raDeg`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_panstarrs`
--

DROP TABLE IF EXISTS `fs_panstarrs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_panstarrs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `candidateID` varchar(20) NOT NULL,
  `ra_deg` double NOT NULL,
  `dec_deg` double NOT NULL,
  `mag` float DEFAULT NULL,
  `magErr` float DEFAULT NULL COMMENT 'Mag error only available in the recurrence data',
  `filter` varchar(10) DEFAULT NULL COMMENT 'Observaton filter',
  `observationMJD` double DEFAULT NULL COMMENT 'Observation date in MJD',
  `discDate` date DEFAULT NULL,
  `discMag` float DEFAULT NULL,
  `suggestedType` varchar(50) DEFAULT NULL,
  `catalogType` varchar(50) DEFAULT NULL,
  `hostZ` float DEFAULT NULL,
  `targetImageURL` varchar(512) DEFAULT NULL,
  `refImageURL` varchar(512) DEFAULT NULL,
  `diffImageURL` varchar(512) DEFAULT NULL,
  `objectURL` varchar(512) DEFAULT NULL,
  `ingested` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Transient Bucket ingest flag.  Has this data been ingested yet?',
  `htm16ID` bigint(20) unsigned DEFAULT NULL,
  `survey` varchar(45) NOT NULL DEFAULT 'PS1',
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `updated` tinyint(4) DEFAULT 0,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `idx_uq_candidateID_discDate` (`candidateID`,`discDate`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `uni_id_mag_mjd` (`candidateID`,`mag`,`observationMJD`),
  KEY `idx_candidateID` (`candidateID`) KEY_BLOCK_SIZE=1024,
  KEY `idx_htm16ID` (`htm16ID`) KEY_BLOCK_SIZE=1024,
  KEY `htm16` (`htm16ID`) KEY_BLOCK_SIZE=1024,
  KEY `ingested` (`ingested`) KEY_BLOCK_SIZE=1024,
  KEY `idx_htm10ID` (`htm13ID`) KEY_BLOCK_SIZE=1024,
  KEY `idx_htm13ID` (`htm13ID`) KEY_BLOCK_SIZE=1024,
  KEY `i_htm10ID` (`htm10ID`) KEY_BLOCK_SIZE=1024,
  KEY `i_htm13ID` (`htm13ID`) KEY_BLOCK_SIZE=1024,
  KEY `i_htm16ID` (`htm16ID`) KEY_BLOCK_SIZE=1024
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_skymapper`
--

DROP TABLE IF EXISTS `fs_skymapper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_skymapper` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `DECL` double DEFAULT NULL COMMENT 'original keyword: DEC',
  `RA` double DEFAULT NULL,
  `bestType` varchar(100) DEFAULT NULL,
  `candidateID` varchar(100) NOT NULL,
  `candidateURL` varchar(1000) DEFAULT NULL,
  `comment` varchar(2000) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `dateLastRead` datetime DEFAULT NULL,
  `diffThumbURL` varchar(1000) DEFAULT NULL,
  `discFilt` varchar(10) DEFAULT NULL,
  `discMJD` double DEFAULT NULL,
  `discMag` double DEFAULT NULL,
  `filt` varchar(10) DEFAULT NULL,
  `mag` double DEFAULT NULL,
  `magerr` double DEFAULT NULL,
  `mjd` double DEFAULT NULL,
  `newThumbURL` varchar(1000) DEFAULT NULL,
  `noneFilt` varchar(10) DEFAULT NULL,
  `noneMJD` double DEFAULT NULL,
  `noneMag` double DEFAULT NULL,
  `numDet` int(11) DEFAULT NULL,
  `refThumbURL` varchar(1000) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `htm16ID` bigint(20) unsigned DEFAULT NULL,
  `survey` varchar(45) DEFAULT 'skymapper',
  `ingested` tinyint(4) DEFAULT 0,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `finderURL` varchar(624) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `cz` double DEFAULT NULL,
  `cx` double DEFAULT NULL,
  `htm20ID` bigint(20) DEFAULT NULL,
  `cy` double DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `candidateid_mjd` (`candidateID`,`mjd`),
  KEY `htm16` (`htm16ID`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`),
  KEY `idx_htm20ID` (`htm20ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_tns_transients`
--

DROP TABLE IF EXISTS `fs_tns_transients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_tns_transients` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `dateCreated` datetime DEFAULT current_timestamp(),
  `decDeg` double NOT NULL,
  `decSex` varchar(100) DEFAULT NULL,
  `discDate` datetime DEFAULT NULL,
  `discMag` double DEFAULT NULL,
  `discMagFilter` varchar(20) DEFAULT NULL,
  `discoverer` varchar(100) DEFAULT NULL,
  `hostName` varchar(100) DEFAULT NULL,
  `hostRedshift` double DEFAULT NULL,
  `objectName` varchar(120) NOT NULL,
  `objectUrl` varchar(100) DEFAULT NULL,
  `raDeg` double NOT NULL,
  `raSex` varchar(100) DEFAULT NULL,
  `survey` varchar(40) DEFAULT NULL,
  `tnsId` int(11) DEFAULT NULL,
  `specType` varchar(20) DEFAULT NULL,
  `transRedshift` double DEFAULT NULL,
  `lastNonDetectionDate` datetime DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `classificationDate` datetime DEFAULT NULL,
  `classificationDateParsed` tinyint(4) DEFAULT 0,
  `lastNonDetectionDateParsed` tinyint(4) DEFAULT 0,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `objectname` (`objectName`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_user_added`
--

DROP TABLE IF EXISTS `fs_user_added`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_user_added` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `candidateID` varchar(70) NOT NULL,
  `ra_deg` double NOT NULL,
  `dec_deg` double NOT NULL,
  `mag` float DEFAULT NULL,
  `magErr` float DEFAULT NULL COMMENT 'Mag error only available in the recurrence data',
  `filter` varchar(10) DEFAULT NULL COMMENT 'Observaton filter',
  `observationMJD` double DEFAULT NULL COMMENT 'Observation date in MJD',
  `discDate` date DEFAULT NULL,
  `discMag` float DEFAULT NULL,
  `suggestedType` varchar(50) DEFAULT NULL,
  `catalogType` varchar(50) DEFAULT NULL,
  `hostZ` float DEFAULT NULL,
  `targetImageURL` varchar(512) DEFAULT NULL,
  `objectURL` varchar(512) DEFAULT NULL,
  `summaryRow` tinyint(1) NOT NULL DEFAULT 1 COMMENT 'Summary row flag. 1 = summary row, 0 = recurrence. There should always be one summary row and at least one recurrence.',
  `ingested` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Transient Bucket ingest flag.  Has this data been ingested yet?',
  `htm16ID` bigint(20) unsigned DEFAULT NULL,
  `survey` varchar(20) DEFAULT NULL,
  `author` varchar(100) NOT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `suggestedClassification` varchar(45) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_uq_candidateID_observationMJD_mag_filter_summaryRow` (`candidateID`,`observationMJD`,`mag`,`filter`,`summaryRow`),
  UNIQUE KEY `idx_uq_candidateID_discDate` (`candidateID`,`discDate`),
  KEY `idx_candidateID` (`candidateID`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fs_ztf`
--

DROP TABLE IF EXISTS `fs_ztf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fs_ztf` (
  `candidateId` bigint(20) DEFAULT NULL,
  `objectId` varchar(50) NOT NULL,
  `raDeg` double DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `mjd` double NOT NULL,
  `fid` tinyint(4) DEFAULT NULL,
  `magpsf` double DEFAULT NULL,
  `sigmapsf` double DEFAULT NULL,
  `isdiffpos` char(1) DEFAULT NULL,
  `rb` float DEFAULT NULL,
  `magzpsci` double DEFAULT NULL,
  `magzpsciunc` double DEFAULT NULL,
  `filt` char(1) DEFAULT NULL,
  `surveyUrl` varchar(200) DEFAULT NULL,
  `tripletImageUrl` varchar(200) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT 0,
  `htm16ID` bigint(20) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `scorr` double DEFAULT NULL,
  `limitingMag` tinyint(4) DEFAULT 0,
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT,
  `magnr` double DEFAULT NULL,
  `sigmagnr` double DEFAULT NULL,
  `distnr` double DEFAULT NULL,
  `distpsnr1` double DEFAULT NULL,
  `sgscore1` double DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `transientBucketId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `uni_objectId_mjd` (`objectId`,`mjd`),
  UNIQUE KEY `candidateId_UNIQUE` (`candidateId`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm10ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `idx_filt` (`filt`),
  KEY `idx_fid` (`fid`),
  KEY `idx_filt_fid` (`fid`,`filt`),
  KEY `idx_transientBucketID` (`transientBucketId`),
  KEY `idx_dateCreated` (`dateCreated`),
  KEY `idx_objectID` (`objectId`),
  KEY `idx_surveyUrl` (`surveyUrl`),
  KEY `idx_tripletImageUrl` (`tripletImageUrl`),
  KEY `idx_mjd` (`mjd`),
  KEY `idx_isdiffpos` (`isdiffpos`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `logs_executable_timings`
--

DROP TABLE IF EXISTS `logs_executable_timings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logs_executable_timings` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `module_name` varchar(200) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `running_time` varchar(100) NOT NULL,
  PRIMARY KEY (`primaryId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `map_survey_marshall_discoveries`
--

DROP TABLE IF EXISTS `map_survey_marshall_discoveries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `map_survey_marshall_discoveries` (
  `columnName` varchar(150) NOT NULL,
  `tns_sources` varchar(150) DEFAULT NULL,
  `tns_photometry` varchar(150) DEFAULT NULL,
  `view_tns_photometry_discoveries` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`columnName`),
  UNIQUE KEY `columnName_UNIQUE` (`columnName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `map_survey_marshall_photometry`
--

DROP TABLE IF EXISTS `map_survey_marshall_photometry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `map_survey_marshall_photometry` (
  `columnName` varchar(150) NOT NULL,
  `tns_photometry` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`columnName`),
  UNIQUE KEY `columnName_UNIQUE` (`columnName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `map_survey_marshall_spectra`
--

DROP TABLE IF EXISTS `map_survey_marshall_spectra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `map_survey_marshall_spectra` (
  `columnName` varchar(150) NOT NULL,
  `tns_spectra` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`columnName`),
  UNIQUE KEY `columnName_UNIQUE` (`columnName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `map_survey_transientbucket`
--

DROP TABLE IF EXISTS `map_survey_transientbucket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `map_survey_transientbucket` (
  `columnName` varchar(150) NOT NULL,
  PRIMARY KEY (`columnName`),
  UNIQUE KEY `columnName_UNIQUE` (`columnName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `marshall_fs_column_map`
--

DROP TABLE IF EXISTS `marshall_fs_column_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marshall_fs_column_map` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `fs_table_name` varchar(45) NOT NULL,
  `fs_survey_name` varchar(45) DEFAULT NULL,
  `transientBucket_column` varchar(45) DEFAULT NULL,
  `fs_table_column` varchar(45) NOT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `unquie_fs_table_name_fs_table_column` (`fs_table_name`,`fs_table_column`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `marshall_sources`
--

DROP TABLE IF EXISTS `marshall_sources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marshall_sources` (
  `marshallId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'The primary key for this table',
  `raDeg` double DEFAULT NULL COMMENT 'RA is decimal degreed',
  `decDeg` double DEFAULT NULL COMMENT 'DEC in decimal degrees',
  `dateCreated` datetime NOT NULL DEFAULT current_timestamp(),
  `sherlockClassification` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`marshallId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `u_marshallId` (`marshallId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `u_raDeg_decDeg` (`raDeg`,`decDeg`) KEY_BLOCK_SIZE=1024,
  KEY `i_marshallId` (`marshallId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `marshall_sources_discoveries`
--

DROP TABLE IF EXISTS `marshall_sources_discoveries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marshall_sources_discoveries` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'The primary key for this table',
  `marshallId` bigint(20) NOT NULL,
  `name` varchar(40) NOT NULL COMMENT 'the name of the transient given by the reporting survey.',
  `survey` varchar(20) NOT NULL COMMENT 'the survey reporting observation of this transient',
  `discoveryPhase` varchar(20) DEFAULT NULL COMMENT 'the discovery phase given by the reporting survey (if any)',
  `surveyObjectUrl` varchar(200) DEFAULT NULL COMMENT 'the url for dedicated webpage of transients supplied by the reporting survey (if any)',
  `transientTypePrediction` varchar(40) DEFAULT NULL COMMENT 'an attempt at predicting the transient type by the reporting survey.',
  `transientTypePredicationSource` varchar(40) DEFAULT NULL COMMENT 'the name of the source/catalogue that was used to predict the transient type',
  `hostRedshift` float DEFAULT NULL COMMENT 'redshift measure for the host',
  `hostRedshiftType` varchar(10) DEFAULT NULL COMMENT 'type of redshift measure for the host galaxy\n',
  `referenceImageUrl` varchar(140) DEFAULT NULL COMMENT 'true or false',
  `targetImageUrl` varchar(140) DEFAULT NULL COMMENT 'true or false',
  `subtractedImageUrl` varchar(140) DEFAULT NULL,
  `tripletImageUrl` varchar(140) DEFAULT NULL,
  `finderImageUrl` varchar(140) DEFAULT NULL,
  `lightcurveURL` varchar(140) DEFAULT NULL,
  `dateCreated` datetime NOT NULL DEFAULT current_timestamp(),
  `masterId` int(11) NOT NULL DEFAULT 0 COMMENT 'If this flag is set (=1) then the transient is assigned this name as it''s master ID. If not set (=0) then there is another entry in this table where the master ID has been set.',
  `raDeg` double NOT NULL,
  `decDeg` double NOT NULL,
  PRIMARY KEY (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `u_primaryId` (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `marshallId_survey` (`marshallId`,`survey`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `i_marshallId` (`marshallId`),
  KEY `i_survey` (`survey`),
  KEY `i_surveyId` (`name`),
  KEY `i_masterId` (`masterId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `marshall_sources_photometry`
--

DROP TABLE IF EXISTS `marshall_sources_photometry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marshall_sources_photometry` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'The primary key for this table',
  `marshallId` bigint(20) NOT NULL,
  `name` varchar(40) NOT NULL COMMENT 'the name of the transient given by the reporting survey.',
  `observationDate` datetime NOT NULL COMMENT 'the survey observation date',
  `observationMJD` double NOT NULL COMMENT 'the survey observation MJD',
  `magnitude` float NOT NULL COMMENT 'the survey magnitude',
  `magnitudeError` float DEFAULT NULL COMMENT 'the survey magnitude error',
  `filter` varchar(20) DEFAULT NULL COMMENT 'survey filter',
  `telescope` varchar(100) DEFAULT NULL,
  `instrument` varchar(100) DEFAULT NULL,
  `dateDeleted` datetime DEFAULT NULL,
  `limitingMag` tinyint(4) DEFAULT 0,
  `dateCreated` datetime NOT NULL DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp(),
  `updated` tinyint(4) DEFAULT 0,
  PRIMARY KEY (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `u_primaryId` (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `u_surveyId_mjd` (`name`,`observationMJD`),
  KEY `i_marshallId` (`marshallId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `marshall_sources_related_files`
--

DROP TABLE IF EXISTS `marshall_sources_related_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marshall_sources_related_files` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'The primary key for this table',
  `marshallId` bigint(20) NOT NULL,
  `dateCreated` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `u_primaryId` (`primaryId`) KEY_BLOCK_SIZE=1024,
  KEY `i_marshallId` (`marshallId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `marshall_sources_spectra`
--

DROP TABLE IF EXISTS `marshall_sources_spectra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marshall_sources_spectra` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'The primary key for this table',
  `marshallId` bigint(20) NOT NULL,
  `name` varchar(40) NOT NULL COMMENT 'the name of the transient given by the reporting survey.',
  `observationDate` datetime DEFAULT NULL COMMENT 'the survey observation date',
  `observationMJD` double NOT NULL COMMENT 'the survey observation MJD',
  `transientRedshift` float DEFAULT NULL COMMENT 'redshift as measured from a spectrum of the transient',
  `transientRedshiftNotes` varchar(40) DEFAULT NULL COMMENT 'transient redshift notes',
  `spectralType` varchar(20) NOT NULL COMMENT 'the spectral classification given by the reporting survey (if any)',
  `telescope` varchar(100) DEFAULT NULL,
  `instrument` varchar(100) DEFAULT NULL,
  `reducer` varchar(100) DEFAULT NULL,
  `dateCreated` datetime NOT NULL DEFAULT current_timestamp(),
  `classificationWRTMax` varchar(45) DEFAULT NULL,
  `classificationPhase` int(11) DEFAULT NULL,
  `survey` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `u_primaryId` (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `u_marshallId_mjd` (`marshallId`,`observationMJD`),
  UNIQUE KEY `u_name_mjd` (`name`,`observationMJD`),
  UNIQUE KEY `u_id_survey_specType` (`spectralType`,`marshallId`,`survey`),
  KEY `i_marshallId` (`marshallId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `marshall_transient_akas`
--

DROP TABLE IF EXISTS `marshall_transient_akas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marshall_transient_akas` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT,
  `transientBucketId` bigint(20) NOT NULL,
  `name` varchar(45) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `uni_transientbucketid_name` (`transientBucketId`,`name`),
  KEY `idx_transientbucketid` (`transientBucketId`),
  KEY `idx_name` (`name`),
  KEY `idx_url` (`url`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `meta_workflow_lists_counts`
--

DROP TABLE IF EXISTS `meta_workflow_lists_counts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meta_workflow_lists_counts` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `listname` varchar(100) DEFAULT NULL,
  `count` mediumint(9) DEFAULT NULL,
  PRIMARY KEY (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `primaryId_UNIQUE` (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `listname_unique` (`listname`) KEY_BLOCK_SIZE=1024
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pessto_marshall_object_summaries`
--

DROP TABLE IF EXISTS `pessto_marshall_object_summaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pessto_marshall_object_summaries` (
  `transientBucketId` bigint(20) NOT NULL COMMENT 'This is set to the primaryKeyId of the **first** entry of this object into the database (i.e. earliest dateCreated)',
  `name` varchar(40) CHARACTER SET utf8 NOT NULL COMMENT 'the name of the transient given by the reporting survey.',
  `survey` varchar(45) CHARACTER SET utf8 DEFAULT NULL COMMENT 'the survey reporting observation of this transient',
  `raDeg` double DEFAULT NULL COMMENT 'RA is decimal degreed',
  `decDeg` double DEFAULT NULL COMMENT 'DEC in decimal degrees',
  `spectralType` varchar(20) CHARACTER SET utf8 DEFAULT NULL COMMENT 'the spectral classification given by the reporting survey (if any)',
  `transientRedshift` float DEFAULT NULL COMMENT 'redshift as measured from a spectrum of the transient'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pessto_papers`
--

DROP TABLE IF EXISTS `pessto_papers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pessto_papers` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `abstract_url` varchar(640) DEFAULT NULL,
  `article_url` varchar(638) DEFAULT NULL,
  `athors` varchar(800) DEFAULT NULL,
  `bibcode` varchar(200) DEFAULT NULL,
  `citations_count` int(11) DEFAULT NULL,
  `citations_url` varchar(642) DEFAULT NULL,
  `dateCreated` datetime DEFAULT NULL,
  `dateLastModified` datetime DEFAULT NULL,
  `dateLastRead` datetime DEFAULT NULL,
  `ejournal_url` varchar(640) DEFAULT NULL,
  `journal` varchar(616) DEFAULT NULL,
  `preprint_url` varchar(640) DEFAULT NULL,
  `pubdate` datetime DEFAULT NULL,
  `refcit_count` tinyint(4) DEFAULT NULL,
  `refcit_url` varchar(636) DEFAULT NULL,
  `title` varchar(800) DEFAULT NULL,
  `authors` varchar(800) DEFAULT NULL,
  PRIMARY KEY (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `bibcode_pubdate` (`bibcode`,`pubdate`) KEY_BLOCK_SIZE=4096
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pesstoobjects`
--

DROP TABLE IF EXISTS `pesstoobjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pesstoobjects` (
  `pesstoObjectsId` int(11) NOT NULL AUTO_INCREMENT COMMENT 'This is the primary ID for all pessto objects. All helper tables with reference this ID to associate data with the pessto object.',
  `transientBucketId` int(11) NOT NULL COMMENT 'the primary ID of the pessto object in the master_sn_list table.',
  `classifiedFlag` tinyint(4) NOT NULL DEFAULT 0,
  `marshallWorkflowLocation` varchar(45) NOT NULL COMMENT 'pessto workflow status flag 01 (cannot be null)',
  `alertWorkflowLocation` varchar(45) NOT NULL COMMENT 'pessto workflow status flag 02 (can be null)',
  `publicStatus` int(11) NOT NULL COMMENT 'the release status of the object',
  `dateAdded` datetime NOT NULL COMMENT 'date the pessto object was added to this database',
  `dateLastModified` datetime NOT NULL COMMENT 'date the entry for the pessto object **in this table** was last modified.',
  `finderChartLocalUrl` varchar(300) DEFAULT NULL,
  `lsq_stamp` tinyint(4) DEFAULT NULL,
  `css_stamp` tinyint(4) DEFAULT NULL,
  `lsq_lightcurve` tinyint(4) DEFAULT NULL,
  `ogle_target_stamp` tinyint(4) DEFAULT NULL,
  `ogle_lightcurve` tinyint(4) DEFAULT NULL,
  `ogle_subtracted_stamp` tinyint(4) DEFAULT NULL,
  `ogle_reference_stamp` tinyint(4) DEFAULT NULL,
  `mls_stamp` tinyint(4) DEFAULT NULL,
  `sss_stamp` tinyint(4) DEFAULT NULL,
  `css_lightcurve` tinyint(4) DEFAULT NULL,
  `sss_lightcurve` tinyint(4) DEFAULT NULL,
  `mls_lightcurve` tinyint(4) DEFAULT NULL,
  `ps1_subtracted_stamp` tinyint(4) DEFAULT NULL,
  `ps1_target_stamp` tinyint(4) DEFAULT NULL,
  `ps1_reference_stamp` tinyint(4) DEFAULT NULL,
  `skymapper_reference_stamp` tinyint(4) DEFAULT NULL,
  `skymapper_subtracted_stamp` tinyint(4) DEFAULT NULL,
  `skymapper_target_stamp` tinyint(4) DEFAULT NULL,
  `ogle_color_context_stamp` tinyint(4) DEFAULT NULL,
  `pi_name` varchar(200) DEFAULT NULL,
  `pi_email` varchar(200) DEFAULT NULL,
  `master_pessto_lightcurve` tinyint(4) DEFAULT NULL,
  `classification_finalised` tinyint(4) NOT NULL DEFAULT 0,
  `master_stamp` tinyint(4) DEFAULT NULL,
  `bsl_stamp` tinyint(4) DEFAULT NULL,
  `observationPriority` tinyint(4) DEFAULT 2,
  `lastTimeReviewed` datetime DEFAULT NULL,
  `mpcMatch` varchar(200) DEFAULT NULL,
  `snoozed` tinyint(4) DEFAULT 0,
  `lastReviewedMag` float DEFAULT NULL,
  `lastReviewedMagDate` datetime DEFAULT NULL,
  `des_target_stamp` tinyint(4) DEFAULT NULL,
  `des_reference_stamp` tinyint(4) DEFAULT NULL,
  `des_subtracted_stamp` tinyint(4) DEFAULT NULL,
  `gaia_stamp` tinyint(4) DEFAULT NULL,
  `ps1_map` tinyint(4) DEFAULT NULL,
  `photometry_catalogue_release` varchar(45) DEFAULT NULL,
  `transient_catalogue_release` varchar(45) DEFAULT NULL,
  `followup_target_release` varchar(45) DEFAULT NULL,
  `pessto_citations` varchar(200) DEFAULT NULL,
  `atlas_target_stamp` tinyint(4) DEFAULT NULL,
  `atlas_subtracted_stamp` tinyint(4) DEFAULT NULL,
  `atlas_reference_stamp` tinyint(4) DEFAULT NULL,
  `atlas_fp_lightcurve` datetime DEFAULT NULL,
  `ztf_stamp` tinyint(4) DEFAULT NULL,
  `user_added_stamp` tinyint(4) DEFAULT NULL,
  `resurrectionCount` tinyint(4) DEFAULT 0,
  PRIMARY KEY (`pesstoObjectsId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `pesstoObjectId_UNIQUE` (`pesstoObjectsId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `masterSnId_UNIQUE` (`transientBucketId`) KEY_BLOCK_SIZE=1024,
  KEY `transientBucketId` (`transientBucketId`),
  KEY `classified` (`classifiedFlag`),
  KEY `mwl` (`marshallWorkflowLocation`),
  KEY `awl` (`alertWorkflowLocation`),
  FULLTEXT KEY `fulltext` (`pi_name`),
  FULLTEXT KEY `fulltext_pi_name` (`pi_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pesstoobjectschangelog`
--

DROP TABLE IF EXISTS `pesstoobjectschangelog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pesstoobjectschangelog` (
  `pesstoObjectsChangeLog` int(11) NOT NULL AUTO_INCREMENT,
  `pesstoObjectsId` int(11) NOT NULL,
  `whatWasChanged` mediumtext NOT NULL,
  `whenChangeOccured` datetime NOT NULL,
  `changeAuthor` varchar(45) NOT NULL,
  PRIMARY KEY (`pesstoObjectsChangeLog`) KEY_BLOCK_SIZE=1024
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pesstoobjectscomments`
--

DROP TABLE IF EXISTS `pesstoobjectscomments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pesstoobjectscomments` (
  `pesstoObjectsCommentsId` int(11) NOT NULL AUTO_INCREMENT,
  `pesstoObjectsId` int(11) NOT NULL,
  `commentAuthor` varchar(50) NOT NULL,
  `dateCreated` datetime NOT NULL,
  `dateLastModified` datetime NOT NULL,
  `removed` tinyint(4) NOT NULL DEFAULT 0,
  `localAttachmentUrl` varchar(300) DEFAULT NULL,
  `comment` longtext NOT NULL,
  PRIMARY KEY (`pesstoObjectsCommentsId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `objectId_date_author_comment` (`pesstoObjectsId`,`dateCreated`,`commentAuthor`,`comment`(90)) KEY_BLOCK_SIZE=1024,
  KEY `pesstoObjectsId` (`pesstoObjectsId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `scheduler_api_calls`
--

DROP TABLE IF EXISTS `scheduler_api_calls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scheduler_api_calls` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT,
  `transientBucketId` bigint(20) NOT NULL,
  `objectName` varchar(50) NOT NULL,
  `magnitude` double DEFAULT NULL,
  `limitingMagnitude` tinyint(4) DEFAULT NULL,
  `apiCallType` varchar(45) DEFAULT NULL,
  `triggerTime` datetime NOT NULL,
  `stampUrl` varchar(200) DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `primaryId_UNIQUE` (`primaryId`),
  UNIQUE KEY `uni_transientbucketid_triggerDate` (`transientBucketId`,`triggerTime`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sherlock_classifications`
--

DROP TABLE IF EXISTS `sherlock_classifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sherlock_classifications` (
  `transient_object_id` bigint(20) NOT NULL,
  `classification` varchar(45) DEFAULT NULL,
  `annotation` mediumtext DEFAULT NULL,
  `summary` varchar(50) DEFAULT NULL,
  `mismatchComment` varchar(500) DEFAULT NULL,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `dateCreated` datetime DEFAULT current_timestamp(),
  `updated` varchar(45) DEFAULT '0',
  `user` varchar(80) DEFAULT NULL,
  `commentDate` datetime DEFAULT NULL,
  `separationArcsec` double DEFAULT NULL,
  PRIMARY KEY (`transient_object_id`),
  KEY `idx_classification` (`classification`),
  KEY `idx_summary` (`summary`),
  KEY `idx_dateLastModified` (`dateLastModified`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 */ /*!50003 TRIGGER `sherlock_classifications_BEFORE_INSERT` BEFORE INSERT ON `sherlock_classifications` FOR EACH ROW
BEGIN
    IF new.classification = "ORPHAN" THEN
        SET new.annotation = "The transient location is not matched against any known catalogued source", new.summary = "No catalogued match";
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 */ /*!50003 TRIGGER `sherlock_classifications_AFTER_INSERT` AFTER INSERT ON `sherlock_classifications` FOR EACH ROW
BEGIN
    update `transientBucket` set `sherlockClassification` = new.classification
					where `transientBucketId`  = new.transient_object_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `sherlock_crossmatches`
--

DROP TABLE IF EXISTS `sherlock_crossmatches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sherlock_crossmatches` (
  `transient_object_id` bigint(20) unsigned DEFAULT NULL,
  `catalogue_object_id` varchar(200) DEFAULT NULL,
  `catalogue_table_id` smallint(5) unsigned DEFAULT NULL,
  `separationArcsec` double DEFAULT NULL,
  `northSeparationArcsec` double DEFAULT NULL,
  `eastSeparationArcsec` double DEFAULT NULL,
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `z` double DEFAULT NULL,
  `scale` double DEFAULT NULL,
  `distance` double DEFAULT NULL,
  `distance_modulus` double DEFAULT NULL,
  `photoZ` double DEFAULT NULL,
  `photoZErr` double DEFAULT NULL,
  `association_type` varchar(45) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `physical_separation_kpc` double DEFAULT NULL,
  `catalogue_object_type` varchar(45) DEFAULT NULL,
  `catalogue_object_subtype` varchar(45) DEFAULT NULL,
  `association_rank` int(11) DEFAULT NULL,
  `catalogue_table_name` varchar(100) DEFAULT NULL,
  `catalogue_view_name` varchar(100) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  `rankScore` double DEFAULT NULL,
  `search_name` varchar(100) DEFAULT NULL,
  `major_axis_arcsec` double DEFAULT NULL,
  `direct_distance` double DEFAULT NULL,
  `direct_distance_scale` double DEFAULT NULL,
  `direct_distance_modulus` double DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `original_search_radius_arcsec` double DEFAULT NULL,
  `catalogue_view_id` int(11) DEFAULT NULL,
  `U` double DEFAULT NULL,
  `UErr` double DEFAULT NULL,
  `B` double DEFAULT NULL,
  `BErr` double DEFAULT NULL,
  `V` double DEFAULT NULL,
  `VErr` double DEFAULT NULL,
  `R` double DEFAULT NULL,
  `RErr` double DEFAULT NULL,
  `I` double DEFAULT NULL,
  `IErr` double DEFAULT NULL,
  `J` double DEFAULT NULL,
  `JErr` double DEFAULT NULL,
  `H` double DEFAULT NULL,
  `HErr` double DEFAULT NULL,
  `K` double DEFAULT NULL,
  `KErr` double DEFAULT NULL,
  `_u` double DEFAULT NULL,
  `_uErr` double DEFAULT NULL,
  `_g` double DEFAULT NULL,
  `_gErr` double DEFAULT NULL,
  `_r` double DEFAULT NULL,
  `_rErr` double DEFAULT NULL,
  `_i` double DEFAULT NULL,
  `_iErr` double DEFAULT NULL,
  `_z` double DEFAULT NULL,
  `_zErr` double DEFAULT NULL,
  `_y` double DEFAULT NULL,
  `_yErr` double DEFAULT NULL,
  `G` double DEFAULT NULL,
  `GErr` double DEFAULT NULL,
  `unkMag` double DEFAULT NULL,
  `unkMagErr` double DEFAULT NULL,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `updated` tinyint(4) DEFAULT 0,
  `classificationReliability` tinyint(4) DEFAULT NULL,
  `transientAbsMag` double DEFAULT NULL,
  `merged_rank` tinyint(4) DEFAULT NULL,
  `W1` double DEFAULT NULL,
  `W1Err` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `key_transient_object_id` (`transient_object_id`),
  KEY `key_catalogue_object_id` (`catalogue_object_id`),
  KEY `idx_separationArcsec` (`separationArcsec`),
  KEY `idx_rank` (`rank`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stats_full_release_overview`
--

DROP TABLE IF EXISTS `stats_full_release_overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_full_release_overview` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `filetype` varchar(200) DEFAULT NULL,
  `numberOfFiles` int(11) DEFAULT NULL,
  `dataVolumeBytes` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stats_ssdr1_overview`
--

DROP TABLE IF EXISTS `stats_ssdr1_overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_ssdr1_overview` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `filetype` varchar(200) DEFAULT NULL,
  `numberOfFiles` int(11) DEFAULT NULL,
  `dataVolumeBytes` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stats_ssdr2_overview`
--

DROP TABLE IF EXISTS `stats_ssdr2_overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_ssdr2_overview` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `filetype` varchar(200) DEFAULT NULL,
  `numberOfFiles` int(11) DEFAULT NULL,
  `dataVolumeBytes` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stats_ssdr3_overview`
--

DROP TABLE IF EXISTS `stats_ssdr3_overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_ssdr3_overview` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `filetype` varchar(200) DEFAULT NULL,
  `numberOfFiles` int(11) DEFAULT NULL,
  `dataVolumeBytes` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tcs_catalogue_tables`
--

DROP TABLE IF EXISTS `tcs_catalogue_tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcs_catalogue_tables` (
  `id` smallint(5) unsigned NOT NULL,
  `table_name` varchar(40) NOT NULL,
  `description` varchar(60) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tcs_helper_catalogue_tables_info`
--

DROP TABLE IF EXISTS `tcs_helper_catalogue_tables_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcs_helper_catalogue_tables_info` (
  `id` smallint(5) unsigned NOT NULL,
  `table_name` varchar(100) DEFAULT NULL,
  `description` varchar(60) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `number_of_rows` bigint(20) DEFAULT NULL,
  `reference_url` varchar(200) DEFAULT NULL,
  `reference_text` varchar(70) DEFAULT NULL,
  `notes` mediumtext DEFAULT NULL,
  `vizier_link` varchar(200) DEFAULT NULL,
  `in_ned` tinyint(4) DEFAULT NULL,
  `object_types` varchar(100) DEFAULT NULL,
  `version_number` varchar(45) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `legacy_table` tinyint(4) DEFAULT 0,
  `old_table_name` varchar(100) DEFAULT NULL,
  `raColName` varchar(45) DEFAULT NULL,
  `decColName` varchar(45) DEFAULT NULL,
  `subTypeColName` varchar(45) DEFAULT NULL,
  `objectNameColName` varchar(100) DEFAULT NULL,
  `redshiftColName` varchar(100) DEFAULT NULL,
  `distanceColName` varchar(45) DEFAULT NULL,
  `object_type_accuracy` tinyint(2) DEFAULT NULL,
  `semiMajorColName` varchar(100) DEFAULT NULL,
  `semiMajorToArcsec` float DEFAULT NULL,
  `transientStream` tinyint(4) DEFAULT 0,
  `filter1ColName` varchar(45) DEFAULT NULL,
  `filterName1ColName` varchar(45) DEFAULT NULL,
  `filterErr1ColName` varchar(45) DEFAULT NULL,
  `filter2ColName` varchar(45) DEFAULT NULL,
  `filterName2ColName` varchar(45) DEFAULT NULL,
  `filterErr2ColName` varchar(45) DEFAULT NULL,
  `filter3ColName` varchar(45) DEFAULT NULL,
  `filterName3ColName` varchar(45) DEFAULT NULL,
  `filterErr3ColName` varchar(45) DEFAULT NULL,
  `filter4ColName` varchar(45) DEFAULT NULL,
  `filterName4ColName` varchar(45) DEFAULT NULL,
  `filterErr4ColName` varchar(45) DEFAULT NULL,
  `filter5ColName` varchar(45) DEFAULT NULL,
  `filterName5ColName` varchar(45) DEFAULT NULL,
  `filterErr5ColName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tcs_helper_catalogue_views_info`
--

DROP TABLE IF EXISTS `tcs_helper_catalogue_views_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcs_helper_catalogue_views_info` (
  `id` smallint(5) unsigned NOT NULL,
  `view_name` varchar(100) DEFAULT NULL,
  `number_of_rows` bigint(20) DEFAULT NULL,
  `object_type` varchar(100) DEFAULT NULL,
  `legacy_view` tinyint(4) DEFAULT 0,
  `old_view_name` varchar(100) DEFAULT NULL,
  `table_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tcs_stats_catalogues`
--

DROP TABLE IF EXISTS `tcs_stats_catalogues`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcs_stats_catalogues` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `all_transient_associations` double DEFAULT NULL,
  `dateCreated` datetime DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `number_of_rows` double DEFAULT NULL,
  `object_types` varchar(100) DEFAULT NULL,
  `table_id` tinyint(4) DEFAULT NULL,
  `table_name` varchar(100) DEFAULT NULL,
  `top_ranked_transient_associations` double DEFAULT NULL,
  `transientStream` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `table_id` (`table_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tns_files`
--

DROP TABLE IF EXISTS `tns_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tns_files` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `TNSId` varchar(55) NOT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateObs` datetime DEFAULT NULL,
  `filename` varchar(200) DEFAULT NULL,
  `spec1phot2` tinyint(4) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `updated` tinyint(4) DEFAULT 0,
  `dateLastModified` datetime DEFAULT NULL,
  `comment` varchar(800) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `tnsid_url` (`TNSId`,`url`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tns_photometry`
--

DROP TABLE IF EXISTS `tns_photometry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tns_photometry` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `TNSId` varchar(20) NOT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `exptime` double DEFAULT NULL,
  `filter` varchar(100) DEFAULT NULL,
  `limitingMag` tinyint(4) DEFAULT NULL,
  `mag` double DEFAULT NULL,
  `magErr` double DEFAULT NULL,
  `magUnit` varchar(100) DEFAULT NULL,
  `objectName` varchar(100) DEFAULT NULL,
  `obsdate` datetime DEFAULT NULL,
  `reportAddedDate` datetime DEFAULT NULL,
  `suggestedType` varchar(100) DEFAULT NULL,
  `survey` varchar(100) DEFAULT NULL,
  `telescope` varchar(100) DEFAULT NULL,
  `updated` tinyint(4) DEFAULT 0,
  `dateLastModified` datetime DEFAULT NULL,
  `remarks` varchar(800) DEFAULT NULL,
  `sourceComment` varchar(800) DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT 0,
  `raDeg` double DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `reportingGroup` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `u_tnsid_obsdate_mag` (`mag`,`obsdate`,`TNSId`),
  UNIQUE KEY `u_tnsid_survey_obsdate` (`TNSId`,`survey`,`obsdate`),
  UNIQUE KEY `u_tnsid_obsdate_objname` (`TNSId`,`obsdate`,`objectName`),
  KEY `idx_transientBucketId` (`transientBucketId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tns_sources`
--

DROP TABLE IF EXISTS `tns_sources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tns_sources` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `TNSId` varchar(20) NOT NULL,
  `TNSName` varchar(20) DEFAULT NULL,
  `dateCreated` datetime DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `decSex` varchar(45) DEFAULT NULL,
  `discDate` datetime DEFAULT NULL,
  `discMag` double DEFAULT NULL,
  `discMagFilter` varchar(45) DEFAULT NULL,
  `discSurvey` varchar(100) DEFAULT NULL,
  `discoveryName` varchar(100) DEFAULT NULL,
  `objectUrl` varchar(200) DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `raSex` varchar(45) DEFAULT NULL,
  `specType` varchar(100) DEFAULT NULL,
  `transRedshift` double DEFAULT NULL,
  `updated` tinyint(4) DEFAULT 0,
  `dateLastModified` datetime DEFAULT NULL,
  `hostName` varchar(100) DEFAULT NULL,
  `hostRedshift` double DEFAULT NULL,
  `survey` varchar(100) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT 0,
  `reportingSurvey` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `tnsid` (`TNSId`),
  KEY `idx_transientBucketId` (`transientBucketId`),
  KEY `idx_ingested` (`ingested`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tns_spectra`
--

DROP TABLE IF EXISTS `tns_spectra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tns_spectra` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `TNSId` varchar(45) NOT NULL,
  `TNSuser` varchar(45) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  `exptime` double DEFAULT NULL,
  `obsdate` datetime DEFAULT NULL,
  `reportAddedDate` datetime DEFAULT NULL,
  `specType` varchar(100) DEFAULT NULL,
  `survey` varchar(100) DEFAULT NULL,
  `telescope` varchar(100) DEFAULT NULL,
  `transRedshift` double DEFAULT NULL,
  `updated` tinyint(4) DEFAULT 0,
  `dateLastModified` datetime DEFAULT NULL,
  `remarks` varchar(800) DEFAULT NULL,
  `sourceComment` varchar(800) DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `discoveryName` varchar(50) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT 0,
  `TNSName` varchar(45) DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `tnsid_survey_obsdate` (`TNSId`,`survey`,`obsdate`),
  UNIQUE KEY `u_tnsid_TNSUser_obsdate` (`TNSId`,`TNSuser`,`obsdate`),
  KEY `idx_transientBucketId` (`transientBucketId`),
  KEY `idx_ingested` (`ingested`),
  KEY `idx_TNSName` (`TNSName`),
  KEY `idx_dateCreated` (`dateCreated`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `transientbucket`
--

DROP TABLE IF EXISTS `transientbucket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transientbucket` (
  `primaryKeyId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'The primary key for this table',
  `transientBucketId` bigint(20) NOT NULL COMMENT 'This is set to the primaryKeyId of the **first** entry of this object into the database (i.e. earliest dateCreated)',
  `masterIDFlag` int(11) NOT NULL DEFAULT 0 COMMENT 'If this flag is set (=1) then the transient is assigned this name as it''s master ID. If not set (=0) then there is another entry in this table where the master ID has been set.',
  `name` varchar(40) NOT NULL COMMENT 'the name of the transient given by the reporting survey.',
  `survey` varchar(45) DEFAULT 'unknown' COMMENT 'the survey reporting observation of this transient',
  `raDeg` double DEFAULT NULL COMMENT 'RA is decimal degreed',
  `decDeg` double DEFAULT NULL COMMENT 'DEC in decimal degrees',
  `raDegErr` double DEFAULT NULL,
  `decDegErr` double DEFAULT NULL,
  `observationDate` datetime DEFAULT NULL COMMENT 'the survey observation date',
  `observationMJD` double DEFAULT NULL COMMENT 'the survey observation MJD',
  `magnitude` float DEFAULT NULL COMMENT 'the survey discovery magnitude',
  `magnitudeError` float DEFAULT NULL,
  `filter` varchar(20) DEFAULT NULL COMMENT 'survey discovery filter',
  `transientRedshift` float DEFAULT NULL COMMENT 'redshift as measured from a spectrum of the transient',
  `transientRedshiftNotes` varchar(40) DEFAULT NULL COMMENT 'transient redshift notes',
  `spectralType` varchar(20) DEFAULT NULL COMMENT 'the spectral classification given by the reporting survey (if any)',
  `discoveryPhase` varchar(20) DEFAULT NULL COMMENT 'the discovery phase given by the reporting survey (if any)',
  `dateCreated` datetime DEFAULT current_timestamp(),
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `surveyObjectUrl` varchar(140) DEFAULT NULL COMMENT 'the url for dedicated webpage of transients supplied by the reporting survey (if any)',
  `transientTypePrediction` varchar(40) DEFAULT NULL COMMENT 'an attempt at predicting the transient type by the reporting survey.',
  `transientTypePredicationSource` varchar(40) DEFAULT NULL COMMENT 'the name of the source/catalogue that was used to predict the transient type',
  `hostRedshift` float DEFAULT NULL COMMENT 'redshift measure for the host',
  `hostRedshiftType` varchar(10) DEFAULT NULL COMMENT 'type of redshift measure for the host galaxy\n',
  `referenceImageUrl` varchar(140) DEFAULT NULL COMMENT 'true or false',
  `targetImageUrl` varchar(140) DEFAULT NULL COMMENT 'true or false',
  `subtractedImageUrl` varchar(140) DEFAULT NULL,
  `tripletImageUrl` varchar(140) DEFAULT NULL,
  `htm16ID` bigint(20) unsigned DEFAULT NULL COMMENT 'HTM Level 16',
  `telescope` varchar(100) DEFAULT NULL,
  `instrument` varchar(100) DEFAULT NULL,
  `reducer` varchar(100) DEFAULT NULL,
  `lastNonDetectionDate` datetime DEFAULT NULL,
  `lastNonDetectionMJD` double DEFAULT NULL,
  `dateLastRead` datetime DEFAULT NULL,
  `finderImageUrl` varchar(140) DEFAULT NULL,
  `lightcurveURL` varchar(140) DEFAULT NULL,
  `classificationWRTMax` varchar(45) DEFAULT NULL,
  `classificationPhase` int(11) DEFAULT NULL,
  `limitingMag` tinyint(4) DEFAULT 0,
  `sherlockClassification` varchar(20) DEFAULT NULL,
  `tmpFlag` int(11) DEFAULT NULL,
  `replacedByRowId` bigint(20) DEFAULT 0,
  `dateDeleted` datetime DEFAULT NULL,
  `updated` tinyint(4) DEFAULT 0,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `cz` double DEFAULT NULL,
  `cx` double DEFAULT NULL,
  `htm20ID` bigint(20) DEFAULT NULL,
  `cy` double DEFAULT NULL,
  PRIMARY KEY (`primaryKeyId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `primaryKey_UNIQUE` (`primaryKeyId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `name_observationmjd_magnitude_filter_survey` (`name`,`observationMJD`,`magnitude`,`filter`,`survey`,`replacedByRowId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `name_observationmjd_magnitude_filter` (`name`,`observationMJD`,`magnitude`,`filter`,`replacedByRowId`),
  UNIQUE KEY `name_survey_obsmjd_decDeg_classification` (`name`,`survey`,`decDeg`,`observationMJD`,`replacedByRowId`,`spectralType`) KEY_BLOCK_SIZE=1024,
  KEY `idx_htm16ID` (`htm16ID`) KEY_BLOCK_SIZE=1024,
  KEY `idx_name` (`name`) KEY_BLOCK_SIZE=1024,
  KEY `tbi` (`transientBucketId`),
  KEY `masterflag` (`masterIDFlag`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `idx_transientBucketId` (`transientBucketId`),
  KEY `idx_replacedByRowId` (`replacedByRowId`),
  KEY `idx_sherlockClassifcaition` (`sherlockClassification`),
  KEY `idx_magnitude` (`magnitude`),
  KEY `idx_htm20ID` (`htm20ID`),
  KEY `idx_dateLastModified` (`dateLastModified`),
  KEY `idx_observationmjd` (`observationMJD`),
  KEY `idx_observationDate` (`observationDate`),
  KEY `idx_surveyObjectUrl` (`surveyObjectUrl`),
  KEY `idx_dateCreated` (`dateCreated`),
  KEY `idx_replace_master` (`replacedByRowId`,`masterIDFlag`),
  KEY `idx_name_transientbucketid` (`name`,`transientBucketId`),
  KEY `idx_survey_datecreated` (`survey`,`dateCreated`),
  KEY `idx_surveyObjectUrl_referenceImageUrl` (`surveyObjectUrl`,`referenceImageUrl`),
  KEY `idx_replaceby_transientbucketid` (`transientBucketId`,`replacedByRowId`),
  FULLTEXT KEY `fulltext` (`name`,`survey`,`surveyObjectUrl`),
  FULLTEXT KEY `fulltext_name_survey_surveyObjectUrl` (`name`,`survey`,`surveyObjectUrl`),
  FULLTEXT KEY `fulltext_name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `transientbucketsummaries`
--

DROP TABLE IF EXISTS `transientbucketsummaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transientbucketsummaries` (
  `transientBucketId` int(11) unsigned NOT NULL,
  `sdss_coverage` tinyint(4) DEFAULT NULL,
  `lastNonDetectionDate` datetime DEFAULT NULL,
  `earliestDetection` datetime DEFAULT NULL,
  `recentClassification` varchar(45) DEFAULT NULL,
  `peakMagnitude` double DEFAULT NULL,
  `absolutePeakMagnitude` decimal(20,17) DEFAULT NULL,
  `distanceMpc` double DEFAULT NULL,
  `has_atel` tinyint(4) DEFAULT NULL,
  `best_redshift` double DEFAULT NULL,
  `masterName` varchar(200) DEFAULT NULL,
  `surveyObjectUrl` varchar(500) DEFAULT NULL,
  `currentMagnitude` double DEFAULT NULL,
  `dateAdded` datetime DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `classificationSurvey` varchar(200) DEFAULT NULL,
  `classificationDate` datetime DEFAULT NULL,
  `transientTypePrediction` varchar(200) DEFAULT NULL,
  `currentMagnitudeEstimate` double DEFAULT NULL,
  `currentMagnitudeEstimateUpdated` datetime DEFAULT NULL,
  `recentSlopeOfLightcurve` double DEFAULT NULL,
  `classificationWRTMax` varchar(45) DEFAULT NULL,
  `classificationPhase` int(11) DEFAULT NULL,
  `classificationAddedBy` varchar(100) DEFAULT NULL,
  `objectAddedToMarshallBy` varchar(100) DEFAULT NULL,
  `currentMagnitudeDate` datetime DEFAULT NULL,
  `lastTBSUpdate` datetime DEFAULT NULL,
  `classificationAddedDate` datetime DEFAULT NULL,
  `sherlockClassification` varchar(20) DEFAULT NULL,
  `earliestMagnitude` double DEFAULT NULL,
  `earliestMagnitudeFilter` varchar(45) DEFAULT NULL,
  `earliestMagnitudeSurvey` varchar(45) DEFAULT NULL,
  `host_redshift` double DEFAULT NULL,
  `gLat` double DEFAULT NULL,
  `gLon` double DEFAULT NULL,
  `separationArcsec` double DEFAULT NULL,
  `currentMagnitudeFilter` varchar(45) DEFAULT NULL,
  `currentMagnitudeSurvey` varchar(45) DEFAULT NULL,
  `updateNeeded` tinyint(4) DEFAULT 1,
  `dateLastModified` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`transientBucketId`) KEY_BLOCK_SIZE=1024,
  KEY `tbi` (`transientBucketId`),
  KEY `masterName` (`masterName`),
  KEY `ra_dec` (`raDeg`,`decDeg`),
  KEY `idx_updateNeeded` (`updateNeeded`),
  KEY `idx_surveyObjectUrl` (`surveyObjectUrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `transients_history_logs`
--

DROP TABLE IF EXISTS `transients_history_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transients_history_logs` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT,
  `transientBucketId` bigint(20) NOT NULL,
  `dateCreated` datetime NOT NULL DEFAULT current_timestamp(),
  `log` varchar(200) NOT NULL,
  PRIMARY KEY (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `unique_index` (`transientBucketId`,`dateCreated`) KEY_BLOCK_SIZE=1024,
  KEY `tbi` (`transientBucketId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `view_fs_crts_css_summary`
--

DROP TABLE IF EXISTS `view_fs_crts_css_summary`;
/*!50001 DROP VIEW IF EXISTS `view_fs_crts_css_summary`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_fs_crts_css_summary` (
  `primaryId` tinyint NOT NULL,
  `circularUrl` tinyint NOT NULL,
  `comment` tinyint NOT NULL,
  `commentIngested` tinyint NOT NULL,
  `dateCreated` tinyint NOT NULL,
  `dateLastModified` tinyint NOT NULL,
  `dateLastRead` tinyint NOT NULL,
  `decDeg` tinyint NOT NULL,
  `filter` tinyint NOT NULL,
  `finderChartUrl` tinyint NOT NULL,
  `finderChartWebpage` tinyint NOT NULL,
  `imagesUrl` tinyint NOT NULL,
  `ingested` tinyint NOT NULL,
  `lightcurveUrl` tinyint NOT NULL,
  `mag` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `observationDate` tinyint NOT NULL,
  `observationMJD` tinyint NOT NULL,
  `raDeg` tinyint NOT NULL,
  `summaryRow` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `surveyObjectUrl` tinyint NOT NULL,
  `targetImageUrl` tinyint NOT NULL,
  `transientTypePrediction` tinyint NOT NULL,
  `uniqueId` tinyint NOT NULL,
  `htm16ID` tinyint NOT NULL,
  `magErr` tinyint NOT NULL,
  `lastNonDetectionDate` tinyint NOT NULL,
  `lastNonDetectionMJD` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_fs_crts_mls_summary`
--

DROP TABLE IF EXISTS `view_fs_crts_mls_summary`;
/*!50001 DROP VIEW IF EXISTS `view_fs_crts_mls_summary`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_fs_crts_mls_summary` (
  `primaryId` tinyint NOT NULL,
  `circularUrl` tinyint NOT NULL,
  `comment` tinyint NOT NULL,
  `commentIngested` tinyint NOT NULL,
  `dateCreated` tinyint NOT NULL,
  `dateLastModified` tinyint NOT NULL,
  `dateLastRead` tinyint NOT NULL,
  `decDeg` tinyint NOT NULL,
  `filter` tinyint NOT NULL,
  `finderChartUrl` tinyint NOT NULL,
  `finderChartWebpage` tinyint NOT NULL,
  `imagesUrl` tinyint NOT NULL,
  `ingested` tinyint NOT NULL,
  `lightcurveUrl` tinyint NOT NULL,
  `mag` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `observationDate` tinyint NOT NULL,
  `observationMJD` tinyint NOT NULL,
  `raDeg` tinyint NOT NULL,
  `summaryRow` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `surveyObjectUrl` tinyint NOT NULL,
  `targetImageUrl` tinyint NOT NULL,
  `transientTypePrediction` tinyint NOT NULL,
  `uniqueId` tinyint NOT NULL,
  `htm16ID` tinyint NOT NULL,
  `magErr` tinyint NOT NULL,
  `lastNonDetectionDate` tinyint NOT NULL,
  `lastNonDetectionMJD` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_fs_crts_sss_summary`
--

DROP TABLE IF EXISTS `view_fs_crts_sss_summary`;
/*!50001 DROP VIEW IF EXISTS `view_fs_crts_sss_summary`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_fs_crts_sss_summary` (
  `primaryId` tinyint NOT NULL,
  `circularUrl` tinyint NOT NULL,
  `comment` tinyint NOT NULL,
  `commentIngested` tinyint NOT NULL,
  `dateCreated` tinyint NOT NULL,
  `dateLastModified` tinyint NOT NULL,
  `dateLastRead` tinyint NOT NULL,
  `decDeg` tinyint NOT NULL,
  `filter` tinyint NOT NULL,
  `finderChartUrl` tinyint NOT NULL,
  `finderChartWebpage` tinyint NOT NULL,
  `imagesUrl` tinyint NOT NULL,
  `ingested` tinyint NOT NULL,
  `lightcurveUrl` tinyint NOT NULL,
  `mag` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `observationDate` tinyint NOT NULL,
  `observationMJD` tinyint NOT NULL,
  `raDeg` tinyint NOT NULL,
  `summaryRow` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `surveyObjectUrl` tinyint NOT NULL,
  `targetImageUrl` tinyint NOT NULL,
  `transientTypePrediction` tinyint NOT NULL,
  `uniqueId` tinyint NOT NULL,
  `htm16ID` tinyint NOT NULL,
  `magErr` tinyint NOT NULL,
  `lastNonDetectionDate` tinyint NOT NULL,
  `lastNonDetectionMJD` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_fs_ogle_summary`
--

DROP TABLE IF EXISTS `view_fs_ogle_summary`;
/*!50001 DROP VIEW IF EXISTS `view_fs_ogle_summary`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_fs_ogle_summary` (
  `primaryId` tinyint NOT NULL,
  `dateCreated` tinyint NOT NULL,
  `dateLastModified` tinyint NOT NULL,
  `dateLastRead` tinyint NOT NULL,
  `decDeg` tinyint NOT NULL,
  `filter` tinyint NOT NULL,
  `ingested` tinyint NOT NULL,
  `lastNonDetectionDate` tinyint NOT NULL,
  `lastNonDetectionMJD` tinyint NOT NULL,
  `lightcurveUrl` tinyint NOT NULL,
  `mag` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `observationDate` tinyint NOT NULL,
  `observationMJD` tinyint NOT NULL,
  `raDeg` tinyint NOT NULL,
  `referenceFitsUrl` tinyint NOT NULL,
  `referenceImageUrl` tinyint NOT NULL,
  `subtractedFitsUrl` tinyint NOT NULL,
  `subtractedImageUrl` tinyint NOT NULL,
  `summaryRow` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `surveyObjectUrl` tinyint NOT NULL,
  `targetFitsUrl` tinyint NOT NULL,
  `targetImageUrl` tinyint NOT NULL,
  `transientTypePrediction` tinyint NOT NULL,
  `htm16ID` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_object_akas`
--

DROP TABLE IF EXISTS `view_object_akas`;
/*!50001 DROP VIEW IF EXISTS `view_object_akas`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_object_akas` (
  `transientBucketId` tinyint NOT NULL,
  `primaryKeyId` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `surveyObjectUrl` tinyint NOT NULL,
  `referenceImageUrl` tinyint NOT NULL,
  `targetImageUrl` tinyint NOT NULL,
  `subtractedImageUrl` tinyint NOT NULL,
  `tripletImageUrl` tinyint NOT NULL,
  `finderImageUrl` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_object_temporal_data`
--

DROP TABLE IF EXISTS `view_object_temporal_data`;
/*!50001 DROP VIEW IF EXISTS `view_object_temporal_data`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_object_temporal_data` (
  `transientBucketId` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `observationDate` tinyint NOT NULL,
  `observationMJD` tinyint NOT NULL,
  `magnitude` tinyint NOT NULL,
  `magnitudeError` tinyint NOT NULL,
  `filter` tinyint NOT NULL,
  `surveyObjectUrl` tinyint NOT NULL,
  `referenceImageUrl` tinyint NOT NULL,
  `targetImageUrl` tinyint NOT NULL,
  `subtractedImageUrl` tinyint NOT NULL,
  `tripletImageUrl` tinyint NOT NULL,
  `telescope` tinyint NOT NULL,
  `instrument` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_objectredshifts`
--

DROP TABLE IF EXISTS `view_objectredshifts`;
/*!50001 DROP VIEW IF EXISTS `view_objectredshifts`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_objectredshifts` (
  `transientBucketId` tinyint NOT NULL,
  `transientRedshift` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_objectspectraltypes`
--

DROP TABLE IF EXISTS `view_objectspectraltypes`;
/*!50001 DROP VIEW IF EXISTS `view_objectspectraltypes`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_objectspectraltypes` (
  `transientBucketId` tinyint NOT NULL,
  `spectralType` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_tns_photometry_discoveries`
--

DROP TABLE IF EXISTS `view_tns_photometry_discoveries`;
/*!50001 DROP VIEW IF EXISTS `view_tns_photometry_discoveries`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_tns_photometry_discoveries` (
  `raDeg` tinyint NOT NULL,
  `decDeg` tinyint NOT NULL,
  `objectName` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `suggestedType` tinyint NOT NULL,
  `hostRedshift` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_transientbucketmaster`
--

DROP TABLE IF EXISTS `view_transientbucketmaster`;
/*!50001 DROP VIEW IF EXISTS `view_transientbucketmaster`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_transientbucketmaster` (
  `primaryKeyId` tinyint NOT NULL,
  `transientBucketId` tinyint NOT NULL,
  `masterIDFlag` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `raDeg` tinyint NOT NULL,
  `decDeg` tinyint NOT NULL,
  `raDegErr` tinyint NOT NULL,
  `decDegErr` tinyint NOT NULL,
  `observationDate` tinyint NOT NULL,
  `observationMJD` tinyint NOT NULL,
  `magnitude` tinyint NOT NULL,
  `magnitudeError` tinyint NOT NULL,
  `filter` tinyint NOT NULL,
  `transientRedshift` tinyint NOT NULL,
  `transientRedshiftNotes` tinyint NOT NULL,
  `spectralType` tinyint NOT NULL,
  `discoveryPhase` tinyint NOT NULL,
  `dateCreated` tinyint NOT NULL,
  `dateLastModified` tinyint NOT NULL,
  `surveyObjectUrl` tinyint NOT NULL,
  `transientTypePrediction` tinyint NOT NULL,
  `transientTypePredicationSource` tinyint NOT NULL,
  `hostRedshift` tinyint NOT NULL,
  `hostRedshiftType` tinyint NOT NULL,
  `referenceImageUrl` tinyint NOT NULL,
  `targetImageUrl` tinyint NOT NULL,
  `subtractedImageUrl` tinyint NOT NULL,
  `tripletImageUrl` tinyint NOT NULL,
  `htm20ID` tinyint NOT NULL,
  `htm16ID` tinyint NOT NULL,
  `cx` tinyint NOT NULL,
  `cy` tinyint NOT NULL,
  `cz` tinyint NOT NULL,
  `telescope` tinyint NOT NULL,
  `instrument` tinyint NOT NULL,
  `reducer` tinyint NOT NULL,
  `lastNonDetectionDate` tinyint NOT NULL,
  `lastNonDetectionMJD` tinyint NOT NULL,
  `dateLastRead` tinyint NOT NULL,
  `finderImageUrl` tinyint NOT NULL,
  `lightcurveURL` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_wiserep_object_summaries`
--

DROP TABLE IF EXISTS `view_wiserep_object_summaries`;
/*!50001 DROP VIEW IF EXISTS `view_wiserep_object_summaries`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_wiserep_object_summaries` (
  `transientBucketId` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `survey` tinyint NOT NULL,
  `raDeg` tinyint NOT NULL,
  `decDeg` tinyint NOT NULL,
  `spectralType` tinyint NOT NULL,
  `transientRedshift` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `webapp_users`
--

DROP TABLE IF EXISTS `webapp_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webapp_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) NOT NULL,
  `secondname` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL DEFAULT '$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1',
  `permissions` varchar(45) NOT NULL DEFAULT 'edit_users',
  PRIMARY KEY (`id`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `first_second` (`firstname`,`secondname`) KEY_BLOCK_SIZE=1024
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_april2016_april2017_stats`
--

DROP TABLE IF EXISTS `zlegacy_april2016_april2017_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_april2016_april2017_stats` (
  `transientBucketId` bigint(20) unsigned NOT NULL,
  `atelNumber` int(11) NOT NULL,
  `classificationDate` datetime DEFAULT NULL,
  `discSurvey` varchar(45) DEFAULT NULL,
  `discMag` double DEFAULT NULL,
  `discDate` datetime DEFAULT NULL,
  `redshift` double DEFAULT NULL,
  `classification` varchar(45) DEFAULT NULL,
  `discName` varchar(100) DEFAULT NULL,
  `tnsName` varchar(100) DEFAULT NULL,
  `atelRa` varchar(45) DEFAULT NULL,
  `atelDec` varchar(45) DEFAULT NULL,
  `classificationPhaseRange` varchar(45) DEFAULT NULL,
  `classificationPhaseDays` int(11) DEFAULT NULL,
  `classificationType` varchar(45) DEFAULT NULL,
  `classificationSubtype` varchar(45) DEFAULT NULL,
  `classificationPhaseBin` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`transientBucketId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_cbats`
--

DROP TABLE IF EXISTS `zlegacy_cbats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_cbats` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `ra` varchar(30) DEFAULT NULL,
  `decl` varchar(30) DEFAULT NULL,
  `hostGalaxy` varchar(60) DEFAULT NULL,
  `dateAndPosition` varchar(60) DEFAULT NULL,
  `offsetWE` varchar(20) DEFAULT NULL,
  `offsetNS` varchar(20) DEFAULT NULL,
  `mag` float DEFAULT NULL,
  `discoveryRef` varchar(40) DEFAULT NULL,
  `positionRef` varchar(40) DEFAULT NULL,
  `snType` varchar(20) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `discoverers` varchar(300) DEFAULT NULL,
  `raDeg` double NOT NULL,
  `decDeg` double NOT NULL,
  `htm20ID` bigint(20) unsigned DEFAULT NULL,
  `htm16ID` bigint(20) unsigned DEFAULT NULL,
  `cx` double DEFAULT NULL,
  `cy` double DEFAULT NULL,
  `cz` double DEFAULT NULL,
  `cbatType` char(8) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name` (`name`),
  KEY `idx_htm20ID` (`htm20ID`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_cbat_type` (`cbatType`),
  KEY `name` (`snType`),
  KEY `ra_dec` (`raDeg`,`decDeg`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_fs_asassn_discoveries`
--

DROP TABLE IF EXISTS `zlegacy_fs_asassn_discoveries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_fs_asassn_discoveries` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `candidateID` varchar(100) DEFAULT NULL,
  `dateCreated` datetime DEFAULT NULL,
  `dec_deg` double DEFAULT NULL,
  `decl` varchar(100) DEFAULT NULL,
  `discDate` datetime DEFAULT NULL,
  `discMag` varchar(100) DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `ra` varchar(100) DEFAULT NULL,
  `ra_deg` double DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT 0,
  `htm16ID` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `candidateid` (`candidateID`),
  KEY `ra_dec` (`dec_deg`,`ra_deg`),
  KEY `htm16` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_fs_brightsnlist_discoveries`
--

DROP TABLE IF EXISTS `zlegacy_fs_brightsnlist_discoveries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_fs_brightsnlist_discoveries` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `dateCreated` datetime DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `discoveryMag` double DEFAULT NULL,
  `discoveryMjd` double DEFAULT NULL,
  `imageUrl` varchar(300) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `objectUrl` varchar(300) DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `survey` varchar(50) DEFAULT 'bright sn list',
  `type` varchar(45) DEFAULT 'SN',
  `ingested` tinyint(4) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `name` (`name`),
  KEY `htm16` (`htm16ID`),
  KEY `ra_dec` (`decDeg`,`raDeg`),
  KEY `ingested` (`ingested`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`),
  KEY `i_htm10ID` (`htm10ID`),
  KEY `i_htm13ID` (`htm13ID`),
  KEY `i_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_fs_lsq`
--

DROP TABLE IF EXISTS `zlegacy_fs_lsq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_fs_lsq` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `candidateID` varchar(20) NOT NULL,
  `ra` varchar(20) DEFAULT NULL,
  `decl` varchar(20) DEFAULT NULL,
  `mag` float DEFAULT NULL,
  `magErr` float DEFAULT NULL COMMENT 'Mag error only available in the recurrence data',
  `observationJD` double DEFAULT NULL COMMENT 'Observation date in JD',
  `discDate` date DEFAULT NULL,
  `discMag` float DEFAULT NULL,
  `suggestedType` varchar(50) DEFAULT NULL,
  `catalogType` varchar(50) DEFAULT NULL,
  `hostZ` float DEFAULT NULL,
  `lastNonDetection` date DEFAULT NULL,
  `tripletImageURL` varchar(512) DEFAULT NULL,
  `obsDate` date DEFAULT NULL,
  `historyURL` varchar(512) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `numPhoto` int(11) DEFAULT NULL,
  `numSpectra` int(11) DEFAULT NULL,
  `specType` varchar(50) DEFAULT NULL,
  `discPhase` int(11) DEFAULT NULL,
  `minObsDate` date DEFAULT NULL,
  `fieldID` int(11) DEFAULT NULL,
  `num3sigpix7` int(11) DEFAULT NULL,
  `num2sigpix7` int(11) DEFAULT NULL,
  `a` float DEFAULT NULL,
  `b` float DEFAULT NULL,
  `symmetry` float DEFAULT NULL,
  `fwhm` float DEFAULT NULL,
  `chipName` varchar(20) DEFAULT NULL,
  `summaryRow` tinyint(1) NOT NULL DEFAULT 1 COMMENT 'Summary row flag. 1 = summary row, 0 = recurrence. There should always be one summary row and at least one recurrence.',
  `ingested` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Transient Bucket ingest flag.  Has this data been ingested yet?',
  `ra_deg` double NOT NULL,
  `dec_deg` double NOT NULL,
  `htm16ID` bigint(20) unsigned DEFAULT NULL,
  `transientZ` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_uq_candidateID_observationJD` (`candidateID`,`observationJD`),
  UNIQUE KEY `idx_uq_candidateID_discDate` (`candidateID`,`discDate`),
  KEY `idx_candidateID` (`candidateID`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `htm16` (`htm16ID`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_fs_lsq_current_summaries`
--

DROP TABLE IF EXISTS `zlegacy_fs_lsq_current_summaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_fs_lsq_current_summaries` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `candidateID` varchar(20) NOT NULL,
  `ra` varchar(20) DEFAULT NULL,
  `decl` varchar(20) DEFAULT NULL,
  `mag` float DEFAULT NULL,
  `magErr` float DEFAULT NULL COMMENT 'Mag error only available in the recurrence data',
  `observationJD` double DEFAULT NULL COMMENT 'Observation date in JD',
  `discDate` date DEFAULT NULL,
  `discMag` float DEFAULT NULL,
  `suggestedType` varchar(50) DEFAULT NULL,
  `catalogType` varchar(50) DEFAULT NULL,
  `hostZ` float DEFAULT NULL,
  `lastNonDetection` date DEFAULT NULL,
  `tripletImageURL` varchar(512) DEFAULT NULL,
  `obsDate` date DEFAULT NULL,
  `historyURL` varchar(512) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `numPhoto` int(11) DEFAULT NULL,
  `numSpectra` int(11) DEFAULT NULL,
  `specType` varchar(50) DEFAULT NULL,
  `discPhase` int(11) DEFAULT NULL,
  `minObsDate` date DEFAULT NULL,
  `fieldID` int(11) DEFAULT NULL,
  `num3sigpix7` int(11) DEFAULT NULL,
  `num2sigpix7` int(11) DEFAULT NULL,
  `a` float DEFAULT NULL,
  `b` float DEFAULT NULL,
  `symmetry` float DEFAULT NULL,
  `fwhm` float DEFAULT NULL,
  `chipName` varchar(20) DEFAULT NULL,
  `summaryRow` tinyint(1) NOT NULL DEFAULT 1 COMMENT 'Summary row flag. 1 = summary row, 0 = recurrence. There should always be one summary row and at least one recurrence.',
  `ingested` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Transient Bucket ingest flag.  Has this data been ingested yet?',
  `ra_deg` double NOT NULL,
  `dec_deg` double NOT NULL,
  `htm16ID` bigint(20) unsigned DEFAULT NULL,
  `transientZ` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_uq_candidateID_observationJD` (`candidateID`,`observationJD`),
  UNIQUE KEY `idx_uq_candidateID_discDate` (`candidateID`,`discDate`),
  KEY `idx_candidateID` (`candidateID`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `htm16` (`htm16ID`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_fs_lsq_discoveries`
--

DROP TABLE IF EXISTS `zlegacy_fs_lsq_discoveries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_fs_lsq_discoveries` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `candidateID` varchar(20) DEFAULT NULL,
  `catalogType` varchar(100) DEFAULT NULL,
  `dateCreated` datetime DEFAULT NULL,
  `dateLastModified` datetime DEFAULT NULL,
  `dateLastRead` datetime DEFAULT NULL,
  `dec_deg` double DEFAULT NULL,
  `decl` varchar(100) DEFAULT NULL,
  `discDate` datetime DEFAULT NULL,
  `discMag` double DEFAULT NULL,
  `discPhase` varchar(100) DEFAULT NULL,
  `historyURL` varchar(1000) DEFAULT NULL,
  `hostZ` double DEFAULT NULL,
  `isFollowed` tinyint(4) DEFAULT NULL,
  `lastNonDetection` datetime DEFAULT NULL,
  `mag` varchar(100) DEFAULT NULL,
  `minObsDate` datetime DEFAULT NULL,
  `numPhoto` tinyint(4) DEFAULT NULL,
  `numSpectra` tinyint(4) DEFAULT NULL,
  `obsDate` datetime DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `ra` varchar(100) DEFAULT NULL,
  `ra_deg` double DEFAULT NULL,
  `specType` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `subtractedLightcurveURL` varchar(300) DEFAULT NULL,
  `suggestedType` varchar(100) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `tripletImageURL` varchar(1000) DEFAULT NULL,
  `transientBucketId` int(11) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT NULL,
  `survey` varchar(45) NOT NULL DEFAULT 'LSQ',
  `transientHistoryLogAdded` tinyint(4) NOT NULL DEFAULT 0,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `candidateid` (`candidateID`),
  KEY `htm16` (`htm16ID`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_fs_lsq_recalibrated_data`
--

DROP TABLE IF EXISTS `zlegacy_fs_lsq_recalibrated_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_fs_lsq_recalibrated_data` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `Detector` varchar(200) DEFAULT NULL,
  `Filename` varchar(200) DEFAULT NULL,
  `MJD` double DEFAULT NULL,
  `PhotSource` varchar(100) DEFAULT NULL,
  `ccd` varchar(100) DEFAULT NULL,
  `counts` double DEFAULT NULL,
  `dateCreated` datetime DEFAULT NULL,
  `dateLastModified` datetime DEFAULT NULL,
  `dateLastRead` datetime DEFAULT NULL,
  `dcounts` double DEFAULT NULL,
  `dzp` double DEFAULT NULL,
  `filter` varchar(100) DEFAULT NULL,
  `magsys` varchar(100) DEFAULT NULL,
  `mjddisc` double DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `nbad` tinyint(4) DEFAULT NULL,
  `zp` double DEFAULT NULL,
  `csvUpdateDate` datetime NOT NULL,
  `magnitude` double DEFAULT NULL,
  `magnitudeError` double DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT 0,
  `dec_deg` double DEFAULT NULL,
  `ra_deg` double DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `Source` varchar(100) DEFAULT NULL,
  `signaltonoise` double DEFAULT NULL,
  `dryxDiscMJD` double DEFAULT NULL,
  `dryxLastNonDetectionMJD` double DEFAULT NULL,
  `PSFDIR` varchar(100) DEFAULT NULL,
  `Telescope` varchar(100) DEFAULT NULL,
  `chi2` varchar(100) DEFAULT NULL,
  `iscoadd` varchar(100) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `name_mjd` (`name`,`MJD`),
  KEY `htm16` (`htm16ID`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_fs_tocp`
--

DROP TABLE IF EXISTS `zlegacy_fs_tocp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_fs_tocp` (
  `primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
  `dateCreated` datetime DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `discoveryMjd` double DEFAULT NULL,
  `filter` varchar(100) DEFAULT NULL,
  `magnitude` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `surveyObjectUrl` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `survey` varchar(45) DEFAULT 'tocp',
  `ingested` tinyint(4) DEFAULT NULL,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `htm13ID` int(11) DEFAULT NULL,
  `htm10ID` int(11) DEFAULT NULL,
  `transientBucketId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `name` (`name`),
  KEY `htm16` (`htm16ID`),
  KEY `ra_dec` (`decDeg`,`raDeg`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_htm10ID` (`htm13ID`),
  KEY `idx_htm13ID` (`htm13ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_lssndb_candidates`
--

DROP TABLE IF EXISTS `zlegacy_lssndb_candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_lssndb_candidates` (
  `cand_id` int(11) unsigned NOT NULL,
  `observer` varchar(20) DEFAULT NULL,
  `obs_date` int(11) DEFAULT NULL,
  `field_id` varchar(10) DEFAULT NULL,
  `user_name` varchar(20) DEFAULT NULL,
  `cand_name` varchar(20) DEFAULT NULL,
  `cand_index` int(11) DEFAULT NULL,
  `sub_index` int(11) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `type` varchar(20) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `jd` double DEFAULT NULL,
  `x` double DEFAULT NULL,
  `y` double DEFAULT NULL,
  `ra` double DEFAULT NULL,
  `dec` double DEFAULT NULL,
  `mag` double DEFAULT NULL,
  `mag_err` double DEFAULT NULL,
  `num_3sig_pix7` int(11) DEFAULT NULL,
  `num_2sig_pix7` int(11) DEFAULT NULL,
  `a` double DEFAULT NULL,
  `b` double DEFAULT NULL,
  `symmetry` double DEFAULT NULL,
  `fwhm` double DEFAULT NULL,
  `fake_index` int(11) DEFAULT NULL,
  `chip_name` varchar(10) DEFAULT NULL,
  `reffilename` varchar(50) DEFAULT NULL,
  `newfilename` varchar(50) DEFAULT NULL,
  `subfilename` varchar(50) DEFAULT NULL,
  `gifname` varchar(50) DEFAULT NULL,
  `nn_dist_ref` double DEFAULT NULL,
  `mag_ref` double DEFAULT NULL,
  `fwhm_ref` double DEFAULT NULL,
  `seeing_ref` double DEFAULT NULL,
  `band` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`cand_id`),
  KEY `cand_name` (`cand_name`),
  KEY `cand_index` (`cand_index`),
  KEY `ra_dec` (`ra`,`dec`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_lssndb_comments`
--

DROP TABLE IF EXISTS `zlegacy_lssndb_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_lssndb_comments` (
  `comment_id` int(11) unsigned NOT NULL,
  `cand_name` varchar(20) DEFAULT NULL,
  `user_name` varchar(20) DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `comment_added` tinyint(4) NOT NULL DEFAULT 0,
  PRIMARY KEY (`comment_id`),
  KEY `cand_name` (`cand_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_lssndb_followup_status`
--

DROP TABLE IF EXISTS `zlegacy_lssndb_followup_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_lssndb_followup_status` (
  `cand_name` varchar(20) DEFAULT NULL,
  `snf` varchar(200) DEFAULT NULL,
  `snf_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `carnegie` varchar(200) DEFAULT NULL,
  `carnegie_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `pessto` varchar(200) DEFAULT NULL,
  `pessto_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `oxford` varchar(200) DEFAULT NULL,
  `oxford_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `berkeley` varchar(200) DEFAULT NULL,
  `berkeley_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `lcogt` varchar(200) DEFAULT NULL,
  `lcogt_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `other` varchar(200) DEFAULT NULL,
  `other_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_lssndb_marshall_comments`
--

DROP TABLE IF EXISTS `zlegacy_lssndb_marshall_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_lssndb_marshall_comments` (
  `id` int(11) unsigned NOT NULL,
  `cand_name` varchar(20) DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `user_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cand_name` (`cand_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_lssndb_marshall_lc_followup`
--

DROP TABLE IF EXISTS `zlegacy_lssndb_marshall_lc_followup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_lssndb_marshall_lc_followup` (
  `id` int(11) unsigned NOT NULL,
  `cand_name` varchar(20) DEFAULT NULL,
  `survey` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cand_name` (`cand_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_lssndb_ms_lightcurves`
--

DROP TABLE IF EXISTS `zlegacy_lssndb_ms_lightcurves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_lssndb_ms_lightcurves` (
  `obs_id` int(11) unsigned NOT NULL,
  `cand_name` varchar(20) DEFAULT NULL,
  `filter` varchar(10) DEFAULT NULL,
  `mjd` double DEFAULT NULL,
  `counts` double DEFAULT NULL,
  `dcounts` double DEFAULT NULL,
  `zp` double DEFAULT NULL,
  `nbad` int(11) DEFAULT NULL,
  `ccd` varchar(10) DEFAULT NULL,
  `dzp` varchar(20) DEFAULT NULL,
  `magsys` varchar(10) DEFAULT NULL,
  `detector` varchar(20) DEFAULT NULL,
  `source` varchar(20) DEFAULT NULL,
  `raDeg` double DEFAULT NULL,
  `decDeg` double DEFAULT NULL,
  `signaltonoise` double DEFAULT NULL,
  `magnitude` double DEFAULT NULL,
  `magnitudeError` double DEFAULT NULL,
  `dryxLastNonDetectionMJD` double DEFAULT NULL,
  `dryxDiscMJD` double DEFAULT NULL,
  `ingested` tinyint(4) DEFAULT 0,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `magnitudeLimit` double DEFAULT NULL,
  PRIMARY KEY (`obs_id`),
  UNIQUE KEY `obs_id` (`obs_id`),
  UNIQUE KEY `name_mjd` (`cand_name`,`mjd`),
  KEY `name_index` (`cand_name`),
  KEY `ingested` (`ingested`),
  KEY `ra_dec` (`raDeg`,`decDeg`),
  KEY `signal` (`signaltonoise`),
  KEY `mjd` (`mjd`),
  KEY `summary` (`summaryRow`),
  KEY `idx_htm16ID` (`htm16ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zlegacy_lssndb_summary`
--

DROP TABLE IF EXISTS `zlegacy_lssndb_summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zlegacy_lssndb_summary` (
  `id` int(11) DEFAULT NULL,
  `cand_name` varchar(20) DEFAULT NULL,
  `disc_date` int(11) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `catalog_type` varchar(40) DEFAULT NULL,
  `simbad_type` varchar(40) DEFAULT NULL,
  `ned_type` varchar(40) DEFAULT NULL,
  `sloan_type` varchar(40) DEFAULT NULL,
  `num_photo` int(11) DEFAULT NULL,
  `num_spectra` int(11) DEFAULT NULL,
  `followup_lead` varchar(20) DEFAULT NULL,
  `avg_ra` double DEFAULT NULL,
  `avg_dec` double DEFAULT NULL,
  `screening_date` datetime DEFAULT NULL,
  `followup_approved` int(11) DEFAULT NULL,
  `spec_type` varchar(20) DEFAULT NULL,
  `disc_mag` double DEFAULT NULL,
  `z` double DEFAULT NULL,
  `disc_phase` int(11) DEFAULT NULL,
  `variable_followup_approved` int(11) DEFAULT NULL,
  `catalog_z` double DEFAULT NULL,
  `latest_nondiscovery_subtraction` int(11) DEFAULT NULL,
  `spectrum_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `spectrum_phase` int(11) DEFAULT NULL,
  `spectrum_source` varchar(40) DEFAULT NULL,
  `min_obs_date` int(11) DEFAULT NULL,
  `last_obs_date` int(11) DEFAULT NULL,
  `last_mag` double DEFAULT NULL,
  `earliest_detection` date DEFAULT NULL,
  `dateCreated` datetime DEFAULT NULL,
  `dateLastModified` datetime DEFAULT NULL,
  `survey` varchar(45) NOT NULL DEFAULT 'LSQ',
  `transientHistoryLogAdded` tinyint(4) DEFAULT 0,
  `subtractedLightcurveUrl` varchar(200) DEFAULT NULL,
  `tripletImageURL` varchar(200) DEFAULT NULL,
  `historyURL` varchar(200) DEFAULT NULL,
  `observationMJD` double DEFAULT NULL,
  `ingested` tinyint(4) NOT NULL DEFAULT 0,
  `summaryRow` tinyint(4) DEFAULT NULL,
  `htm16ID` bigint(20) DEFAULT NULL,
  `cz` double DEFAULT NULL,
  `cx` double DEFAULT NULL,
  `htm20ID` bigint(20) DEFAULT NULL,
  `cy` double DEFAULT NULL,
  `qubId` bigint(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`qubId`),
  UNIQUE KEY `qubId_UNIQUE` (`qubId`),
  UNIQUE KEY `cand_name_type` (`cand_name`,`type`),
  KEY `htm20` (`htm20ID`),
  KEY `htm16` (`htm16ID`),
  KEY `ingested` (`ingested`),
  KEY `summaryRow` (`summaryRow`),
  KEY `cand_name` (`cand_name`),
  KEY `ra_dec` (`avg_ra`,`avg_dec`),
  KEY `idx_htm20ID` (`htm20ID`),
  KEY `idx_htm16ID` (`htm16ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'marshall'
--
/*!50003 DROP FUNCTION IF EXISTS `does_column_exist` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  FUNCTION `does_column_exist`(table_name_IN VARCHAR(100), column_name_IN VARCHAR(100)) RETURNS int(11)
RETURN (
    SELECT COUNT(COLUMN_NAME) 
    FROM INFORMATION_SCHEMA.columns 
    WHERE TABLE_SCHEMA = DATABASE() 
    AND TABLE_NAME = table_name_IN 
    AND COLUMN_NAME = column_name_IN
) ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_table_column` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `create_table_column`(
    IN table_name_IN VARCHAR(100)
    , IN column_name_IN VARCHAR(100)
    , IN column_definition_IN VARCHAR(100)
)
BEGIN

    SET @columnExists = does_column_exist(table_name_IN, column_name_IN);
    IF (@columnExists = 0) THEN

        SET @ddl = CONCAT('ALTER TABLE ', table_name_IN);
        SET @ddl = CONCAT(@ddl, ' ', 'ADD COLUMN') ;
        SET @ddl = CONCAT(@ddl, ' ', column_name_IN);
        SET @ddl = CONCAT(@ddl, ' ', column_definition_IN);

        PREPARE stmt FROM @ddl;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

    END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_new_marshall_objects` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `insert_new_marshall_objects`()
BEGIN
INSERT INTO pesstoObjects (
		pesstoObjectsId,
		transientBucketId,
		classifiedFlag,
		marshallWorkflowLocation,
		alertWorkflowLocation,
		publicStatus,
		dateAdded,
		dateLastModified)  
	SELECT 
		distinct transientBucketId, transientBucketId, 0, "Inbox", 'Pending Classification', 1, now(), now()
	FROM
		transientBucket
	WHERE
		transientBucketId NOT IN (SELECT 
				transientBucketId
			FROM
				pesstoObjects) AND transientBucketId > 0;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_new_transients_into_transientbucketsummaries` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `insert_new_transients_into_transientbucketsummaries`()
BEGIN
-- ADD NEW TRANSIENTS TO THE transientBucketSummaries TABLE
INSERT ignore INTO transientBucketSummaries (transientBucketId)
select distinct transientBucketId from transientBucket where replacedByRowId = 0 and transientBucketId != 0 and masterIDFlag = 1;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_object_comment` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `insert_object_comment`(transientBucketId_IN BIGINT(11), author_in VARCHAR(100), comment_in VARCHAR(500))
BEGIN
	INSERT INTO pesstoObjectsComments (pesstoObjectsId,
                                                    dateCreated,
                                                    dateLastModified,
                                                    commentAuthor,
                                                    comment
                                                  )
                VALUES (transientBucketId_IN,NOW(),NOW(),author_in,comment_in);

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `resurrect_objects` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `resurrect_objects`()
BEGIN
-- SELECT INTERESTING SOURCE 
-- BRIGHTER THAN 19.5
-- UPDATED RECENTLY
-- ARCHIVED/FOLLOW UP COMPLETE
insert into transients_history_logs (transientBucketId, log) (SELECT 
    s.transientBucketId, "moved to 'inbox' by marshall's object resurrector"
FROM
    transientBucketSummaries s,
    pesstoObjects p
WHERE
    currentMagnitudeEstimate < 19.5
        AND currentMagnitudeEstimate > 3.0
        AND p.resurrectionCount < 5
        AND sherlockClassification not in ('VS','BS','CV','AGN')
        AND (p.lastTimeReviewed < s.currentMagnitudeEstimateUpdated)
        AND (currentMagnitudeEstimate < p.lastReviewedMag)
        AND currentMagnitudeDate > NOW() - INTERVAL 10 DAY
        AND (p.marshallWorkflowLocation = 'archive'
		OR p.marshallWorkflowLocation = 'followup complete')
        AND s.transientBucketId = p.transientBucketId);
        
-- UPDATE SNOOZED FLAG
update pesstoObjects set snoozed = 2, marshallWorkflowLocation = "inbox", resurrectionCount = resurrectionCount+1  where transientBucketId in (select * from (SELECT 
    s.transientBucketId
FROM
    transientBucketSummaries s,
    pesstoObjects p
WHERE
    currentMagnitudeEstimate < 19.5
        AND currentMagnitudeEstimate > 3.0
        AND p.resurrectionCount < 5
        AND sherlockClassification not in ('VS','BS','CV','AGN')
        AND (p.lastTimeReviewed < s.currentMagnitudeEstimateUpdated)
        AND (currentMagnitudeEstimate < p.lastReviewedMag)
        AND currentMagnitudeDate > NOW() - INTERVAL 10 DAY
        AND (p.marshallWorkflowLocation = 'archive'
        OR p.marshallWorkflowLocation = 'followup complete')
        AND s.transientBucketId = p.transientBucketId) as a);
        
-- MOVE CLASSIFIED SOURCES OUT OF THE INBOX & CLASSIFICATION QUEUE
UPDATE pesstoObjects 
SET 
    classifiedFlag = 1
WHERE
    transientBucketId IN (SELECT 
            *
        FROM
            (SELECT DISTINCT
                transientBucketId
            FROM
                transientBucket
            WHERE
                (spectralType IS NOT NULL
                    AND transientBucketId NOT IN (SELECT 
                        transientBucketId
                    FROM
                        pesstoObjects
                    WHERE
                        classifiedFlag = 1))) AS a);
                        
-- INSERT HISTORY LOG
insert into transients_history_logs  (transientBucketId, log) SELECT 
                pesstoObjectsId, CONCAT("moved from ",marshallWorkflowLocation, " to 'review for followup' by marshall code")
            FROM
                pesstoObjects
            WHERE
                marshallWorkflowLocation in ('pending classification', 'inbox')
                    AND classifiedFlag = 1;

-- MOVE CLASSIFIED SOURCES
UPDATE pesstoObjects 
SET 
    marshallWorkflowLocation = 'review for followup',
    snoozed = 0
WHERE
    pesstoObjectsId IN (SELECT 
            *
        FROM
            (SELECT 
                pesstoObjectsId
            FROM
                pesstoObjects
            WHERE
                marshallWorkflowLocation in ('pending classification', 'inbox')
                    AND classifiedFlag = 1) AS alias);
        
-- UPDATE LAST REVIEWED TIME
update pesstoObjects set lastTimeReviewed = NOW();
        

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sync_marshall_feeder_survey_transientBucketId` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `sync_marshall_feeder_survey_transientBucketId`(ARG_fs_table varchar(45))
BEGIN
	set @fs_table = convert(ARG_fs_table using utf8mb4) collate utf8mb4_general_ci;
    
	
	set @object = (select fs_table_column from marshall_fs_column_map where transientBucket_column = "name" and fs_table_name = @fs_table);  
    
    set @survey = (select fs_survey_name from marshall_fs_column_map where fs_table_name = @fs_table limit 1);  
    set @magCol = (select fs_table_column from marshall_fs_column_map where transientBucket_column = "magnitude" and fs_table_name = @fs_table);
    if @magCol is not null then 
		set @magCol = concat('and ',@magCol,' is not null');
	else
		set @magCol = "";
	end if;
    
    set @myquery = concat('UPDATE ',@fs_table,' a
INNER JOIN 
transientBucket b
ON a.',@object,' = b.name
set a.transientBucketId = b.transientBucketId
where a.transientBucketId IS NULL;');
	PREPARE stmt FROM @myquery;
	EXECUTE stmt;
    
    
    if @survey is not null then 
		set @tbcolumns = (select CONCAT_WS(',',GROUP_CONCAT(transientBucket_column  order  by primaryId),'survey') from marshall_fs_column_map where fs_table_name = @fs_table);
		set @fscolumns = (select GROUP_CONCAT(fs_table_column  order  by primaryId) from marshall_fs_column_map where fs_table_name = ARG_fs_table);
		set @myquery = concat('insert ignore into transientBucket (transientBucketId,',@tbcolumns,') select transientBucketId,',@fscolumns,',"',@survey,'" from ',@fs_table,' where ingested = 0 and transientBucketId is not null ',@magCol,';' );
	else
		set @tbcolumns = (select GROUP_CONCAT(transientBucket_column  order  by primaryId) from marshall_fs_column_map where fs_table_name = @fs_table);
		set @fscolumns = (select GROUP_CONCAT(fs_table_column  order  by primaryId) from marshall_fs_column_map where fs_table_name = @fs_table);
		set @myquery = concat('insert ignore into transientBucket (transientBucketId,',@tbcolumns,') select transientBucketId,',@fscolumns,' from ',@fs_table,' where ingested = 0 and transientBucketId is not null ',@magCol,';' );
	end if;
    PREPARE stmt FROM @myquery;
    EXECUTE stmt;
    
    
    set @myquery = concat('update ',ARG_fs_table,' set ingested = 1 where transientBucketId is not null and ingested = 0 ',@magCol,';');
	PREPARE stmt FROM @myquery;
    EXECUTE stmt;
    
    
    set @myquery = 'insert into sherlock_classifications (transient_object_id) select distinct transientBucketId from transientBucketSummaries ON DUPLICATE KEY UPDATE  transient_object_id = transientBucketId;';
    PREPARE stmt FROM @myquery;
    EXECUTE stmt;
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_fs_atlas_forced_phot` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_fs_atlas_forced_phot`()
BEGIN
	-- update fs_atlas_forced_phot set apfit = (mag-zp+2.5*log10(peakfit * major * minor / texp))  where peakfit is not null and major is not null and minor is not null and texp is not null and limiting_mag = 0 and apfit is null;
	-- update fs_atlas_forced_phot set apfit = (mag-zp+2.5*log10(dpeak * major * minor * snr / texp)) where dpeak is not null and snr is not null and major is not null and minor is not null and texp is not null and limiting_mag = 1 and apfit is null;
	update fs_atlas_forced_phot set marshall_limiting_mag = 1 where snr < 5.0 and dpeak is not null and marshall_limiting_mag is null;
	update fs_atlas_forced_phot set marshall_limiting_mag =  0 where snr >= 5.0 and dpeak is not null and marshall_limiting_mag is null;
	update fs_atlas_forced_phot set marshall_mag =  mag where snr >= 5.0 and dpeak is not null and marshall_mag is null;
	update fs_atlas_forced_phot set marshall_mag_error = dm where snr >= 5.0 and dpeak is not null and marshall_mag_error is null;
	update fs_atlas_forced_phot set marshall_mag = cast(mag-2.5*log10(5/snr) as decimal(10,2)) where dpeak is not null and limiting_mag = 1 and mag is not null and marshall_mag is null;
	update fs_atlas_forced_phot set marshall_mag = cast(mag-2.5*log10(dpeak*5/peakfit) as decimal(10,2)) where dpeak is not null and limiting_mag = 0 and mag is not null and snr < 5 and marshall_mag is null;
	update fs_atlas_forced_phot set fnu =(pow(10,-(48.6 + zp)/2.5) * pow(10,-apfit/2.5) * (peakfit*major*minor/texp)) where apfit is not null and zp is not null and peakfit is not null and fnu is null;
	update fs_atlas_forced_phot set fnu_error = (pow(10,-(48.6 + zp)/2.5) * pow(10,-apfit/2.5) * (dpeak*major*minor/texp)) where apfit is not null and zp is not null and dpeak is not null and fnu_error is null;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_fs_ztf` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_fs_ztf`()
BEGIN
	update fs_ztf set filt = 'g' where fid = 1 and filt is null;
	update fs_ztf set filt = 'r' where fid = 2 and filt is null;
	update fs_ztf set filt = 'i' where fid = 3 and filt is null;
    update fs_ztf set primaryId = candidateId where primaryId is null;
	update fs_ztf set  surveyUrl = CONCAT("http://lasair.roe.ac.uk/object/",objectId) where surveyUrl is null;
	update fs_ztf set tripletImageUrl = concat("http://lasair.roe.ac.uk/lasair/static/ztf/stamps/jpg/",SUBSTRING(candidateId, 1, 3),"/candid",candidateId,".jpg") where tripletImageUrl is null and candidateId is not null;

## UPDATE NONDETECTION COORDINATES
update fs_ztf a, (SELECT 
    objectId, raDeg, decDeg
FROM
    fs_ztf
WHERE
    limitingMag = 0
        AND objectId IN (SELECT 
            *
        FROM
            (SELECT DISTINCT
                objectId
            FROM
                fs_ztf
            WHERE
                limitingMag = 1 AND raDeg IS NULL) AS z) group by objectId) b set a.raDeg=b.raDeg,a.decDeg=b.decDeg where a.objectId=b.objectId and a.raDeg is null;

-- DELETE NULL RA
delete from fs_ztf where raDeg is null and limitingMag = 0;

-- FILTER OUT NEGATIVE DETECTIONS
update fs_ztf set ingested = 1 where (isdiffpos = "f" or  isdiffpos = "0") and ingested  = 0;

-- DELETE OLD DETECTIONS
delete from fs_ztf where mjd < (TO_SECONDS(UTC_TIMESTAMP())/(3600*24)-678941-42) and transientBucketId is not null and ingested = 1;

-- DELETE BAD RA
delete from fs_ztf where raDeg is null;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_inbox_auto_archiver` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_inbox_auto_archiver`()
BEGIN
	-- CLEAR OUT ZTF SOURCES .. FAINT AND LOW GALACTIC ANGLE
UPDATE transientBucketSummaries t,
        pesstoObjects p 
    SET 
        marshallWorkflowLocation = 'archive'
    WHERE
        t.mastername LIKE 'ZTF%%'
            AND (t.currentMagnitude > 20.0
            OR ABS(t.gLat) < 10)
            AND p.transientBucketId = t.transientBucketId
            AND marshallWorkflowLocation = "inbox" ;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_sherlock_crossmatches` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_sherlock_crossmatches`()
BEGIN
	-- ADD ORIGINAL SEARCH RADIUS TO MERGED RANKINGS
	update sherlock_crossmatches a
	inner join (select s.id, min(t.original_search_radius_arcsec) as radius from sherlock_crossmatches s
	inner join sherlock_crossmatches t
	where s.transient_object_id=t.transient_object_id
	and s.original_search_radius_arcsec = 0
	and s.rank is not null and s.rank=t.merged_rank group by concat(s.transient_object_id,t.merged_rank )) as b
	set a.original_search_radius_arcsec=b.radius
	where a.id=b.id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_sherlock_xmatch_counts` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_sherlock_xmatch_counts`()
BEGIN
-- ALL TRANSIENTS ASSOICATED WITH CATALOGUES
UPDATE tcs_stats_catalogues t 
LEFT JOIN
(SELECT 
    catalogue_table_id, count(*) as 'all_transient_associations'
FROM
    (SELECT DISTINCT
        c.transient_object_id, c.catalogue_table_id
    FROM
        sherlock_crossmatches c, transientBucketSummaries s
    WHERE
        s.transientBucketId = c.transient_object_id) AS alais group by catalogue_table_id) o 
ON t.table_id = o.catalogue_table_id
set t.all_transient_associations=o.all_transient_associations;

update tcs_stats_catalogues set all_transient_associations = 0 where all_transient_associations is null;

-- TOP RANKED TRANSIENTS ASSOICATED WITH CATALOGUES
UPDATE tcs_stats_catalogues t 
LEFT JOIN
(SELECT 
    catalogue_table_id, count(*) as 'top_ranked_transient_associations'
FROM
    (SELECT DISTINCT
        c.transient_object_id, c.catalogue_table_id
    FROM
        sherlock_crossmatches c, transientBucketSummaries s
    WHERE
        s.transientBucketId = c.transient_object_id and c.rank=1) AS alais group by catalogue_table_id) o 
ON t.table_id = o.catalogue_table_id
set t.top_ranked_transient_associations=o.top_ranked_transient_associations;

update tcs_stats_catalogues set top_ranked_transient_associations = 0 where top_ranked_transient_associations is null;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_single_transientbucket_summary` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_single_transientbucket_summary`(
	IN thisID BIGINT(20)
)
BEGIN



UPDATE pesstoObjects 
SET 
    classifiedFlag = 1
WHERE
    transientBucketId IN (SELECT 
            *
        FROM
            (SELECT DISTINCT
                transientBucketId
            FROM
                transientBucket
            WHERE
                (spectralType IS NOT NULL
                    AND transientBucketId = thisID)) AS a);
                        
insert into transients_history_logs  (transientBucketId, log) SELECT 
                pesstoObjectsId, CONCAT("moved from ",marshallWorkflowLocation, " to 'review for followup' by marshall code")
            FROM
                pesstoObjects
            WHERE
                marshallWorkflowLocation in ('pending classification', 'inbox')
                    AND classifiedFlag = 1;

UPDATE pesstoObjects 
SET 
    marshallWorkflowLocation = 'review for followup',
    snoozed = 0
WHERE
    pesstoObjectsId IN (SELECT 
            *
        FROM
            (SELECT 
                pesstoObjectsId
            FROM
                pesstoObjects
            WHERE
                marshallWorkflowLocation in ('pending classification', 'inbox')
                    AND classifiedFlag = 1 and transientBucketId = thisID) AS alias);
                    

INSERT INTO pesstoObjects (
		pesstoObjectsId,
		transientBucketId,
		classifiedFlag,
		marshallWorkflowLocation,
		alertWorkflowLocation,
		publicStatus,
		dateAdded,
		dateLastModified)  
	SELECT 
		transientBucketId, transientBucketId, 0, "Inbox", 'Pending Classification', 1, now(), now()
	FROM
		transientBucket
	WHERE
		transientBucketId NOT IN (SELECT 
				transientBucketId
			FROM
				pesstoObjects) AND transientBucketId > 0 and transientBucketId = thisID and masterIDFlag = 1;

INSERT ignore INTO transientBucketSummaries (transientBucketId)
select distinct transientBucketId from transientBucket where replacedByRowId = 0 and transientBucketId != 0 and transientBucketId = thisID;


UPDATE transientBucketSummaries 
SET 
    updateNeeded = 1
WHERE
    transientBucketId = thisId;	

UPDATE transientBucketSummaries s,
    transientBucket t 
SET 
    s.masterName = t.name,
    s.surveyObjectUrl = t.surveyObjectUrl
WHERE
    masterIdFlag = 1 AND replacedByRowId = 0
        AND s.transientBucketId = t.transientBucketId
        AND t.transientBucketId=thisID;
	

UPDATE transientBucket t,
    transientBucketSummaries s 
SET 
    s.surveyObjectUrl = t.surveyObjectUrl
WHERE
    t.surveyObjectUrl IS NOT NULL
        AND s.surveyObjectUrl IS NULL
        AND t.transientBucketId = s.transientBucketId
        AND t.surveyObjectUrl NOT LIKE '%%astronomerstelegram%%'
        AND t.surveyObjectUrl NOT LIKE '%%roche%%'
        AND replacedByRowId = 0
        AND masterIDFlag = 1
        AND t.transientBucketId=thisID;

UPDATE transientBucket t,
    transientBucketSummaries s 
SET 
    s.surveyObjectUrl = t.surveyObjectUrl
WHERE
    t.surveyObjectUrl IS NOT NULL
        AND s.surveyObjectUrl IS NULL
        AND t.transientBucketId = s.transientBucketId
        AND t.surveyObjectUrl NOT LIKE '%%astronomerstelegram%%'
        AND t.surveyObjectUrl NOT LIKE '%%roche%%'
        AND replacedByRowId = 0
        AND t.transientBucketId=thisID;
	

UPDATE transientBucketSummaries s,
    transientBucket t 
SET 
    s.objectAddedToMarshallBy = t.reducer
WHERE
    t.reducer IS NOT NULL
        AND t.spectralType IS NULL
        AND t.transientBucketId = s.transientBucketId
        AND replacedByRowId = 0
        AND s.updateNeeded = 1
        AND t.transientBucketId=thisID;
	

UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        transientBucketId,
            AVG(raDeg) AS raDeg,
            AVG(decDeg) AS decDeg,
            MIN(dateCreated) AS dateAdded,
            MIN(magnitude) AS peakMagnitude
    FROM
        transientBucket
    WHERE
		transientBucketId=thisID and
        replacedByRowId = 0 AND limitingMag = 0
            AND magnitude IS NOT NULL
            AND magnitude > 0.0
            AND magnitude < 25.0
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS a
    ORDER BY transientBucketId) t 
SET 
    s.raDeg = t.raDeg,
    s.decDeg = t.decDeg,
    s.dateAdded = t.dateAdded,
    s.peakMagnitude = t.peakMagnitude
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1
        AND t.transientBucketId=thisID;

UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        transientBucketId,
            AVG(raDeg) AS raDeg,
            AVG(decDeg) AS decDeg
    FROM
        transientBucket
    WHERE
		transientBucketId=thisID and
        replacedByRowId = 0
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                raDeg IS NULL AND updateNeeded = 1)
    GROUP BY transientBucketId) AS a
    ORDER BY transientBucketId) t 
SET 
    s.raDeg = t.raDeg,
    s.decDeg = t.decDeg
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1
        AND t.transientBucketId=thisID;

UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        transientBucketId, MIN(hostRedshift) AS host_redshift
    FROM
        transientBucket
    WHERE
		transientBucketId=thisID and
        replacedByRowId = 0
            AND hostRedshift IS NOT NULL
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS a
    ORDER BY transientBucketId) t 
SET 
    s.host_redshift = t.host_redshift
WHERE
    s.transientBucketId = t.transientBucketId
        AND updateNeeded = 1
        AND t.transientBucketId=thisID;

UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        a.transientBucketId,
            a.observationDate AS earliestDetection,
            a.magnitude AS earliestMagnitude,
            a.filter AS earliestMagnitudeFilter,
            a.survey AS earliestMagnitudeSurvey
    FROM
        transientBucket a
    JOIN (SELECT 
        MIN(observationDate) AS minval, transientBucketId
    FROM
        transientBucket
    WHERE
		transientBucketId=thisID and
        magnitude IS NOT NULL
            AND limitingMag = 0
            AND replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS b ON a.transientBucketId = b.transientBucketId
        AND a.observationDate = b.minval
    WHERE
        a.limitingMag = 0
            AND a.replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND a.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
				transientBucketId=thisID and
                updateNeeded = 1)
    GROUP BY transientBucketId) AS c
    ORDER BY transientBucketId) t 
SET 
    s.earliestDetection = t.earliestDetection,
    s.earliestMagnitude = t.earliestMagnitude,
    s.earliestMagnitudeFilter = t.earliestMagnitudeFilter,
    s.earliestMagnitudeSurvey = t.earliestMagnitudeSurvey
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1
        AND t.transientBucketId=thisID;


UPDATE transientBucketSummaries a,
    (SELECT 
        *
    FROM
        (SELECT 
        s.transientBucketId,
            MAX(t.lastNonDetectionDate) AS lastNonDetectionDate
    FROM
        transientBucket t, transientBucketSummaries s
    WHERE
		t.transientBucketId=thisID and
        t.lastNonDetectionDate < s.earliestDetection
            AND s.transientBucketId = t.transientBucketId
            AND replacedByRowId = 0
            AND t.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
				transientBucketId=thisID and
                updateNeeded = 1)
    GROUP BY s.transientBucketId) AS c
    ORDER BY transientBucketId) b 
SET 
    a.lastNonDetectionDate = b.lastNonDetectionDate
WHERE
    a.transientBucketId = b.transientBucketId
        AND a.updateNeeded = 1
        AND a.transientBucketId=thisID;
    

UPDATE transientBucketSummaries a,
    (SELECT 
        *
    FROM
        (SELECT 
        s.transientBucketId,
            MAX(t.observationDate) AS lastNonDetectionDate
    FROM
        transientBucket t, transientBucketSummaries s
    WHERE
		t.transientBucketId=thisID and
        t.observationDate < s.earliestDetection
            AND (t.observationDate > s.lastNonDetectionDate
            OR s.lastNonDetectionDate IS NULL)
            AND s.transientBucketId = t.transientBucketId
            AND replacedByRowId = 0
            AND t.limitingMag = 1
            AND t.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY s.transientBucketId) AS a
    ORDER BY transientBucketId) b 
SET 
    a.lastNonDetectionDate = b.lastNonDetectionDate
WHERE
    a.transientBucketId = b.transientBucketId
        AND a.updateNeeded = 1
        AND a.transientBucketId=thisID;


UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        a.transientBucketId,
            a.observationDate AS currentMagnitudeDate,
            a.magnitude AS currentMagnitude,
            a.filter AS currentMagnitudeFilter,
            a.survey AS currentMagnitudeSurvey
    FROM
        transientBucket a
    JOIN (SELECT 
        *
    FROM
        (SELECT 
        MAX(observationDate) AS maxval, transientBucketId
    FROM
        transientBucket
    WHERE
		transientBucketId=thisID and
        magnitude IS NOT NULL
            AND limitingMag = 0
            AND replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS d
    ORDER BY transientBucketId) AS b ON a.transientBucketId = b.transientBucketId
        AND a.observationDate = b.maxval
    WHERE
        a.limitingMag = 0
            AND a.replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND a.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS c
    ORDER BY transientBucketId) t 
SET 
    s.currentMagnitudeDate = t.currentMagnitudeDate,
    s.currentMagnitude = t.currentMagnitude,
    s.currentMagnitudeFilter = t.currentMagnitudeFilter,
    s.currentMagnitudeSurvey = t.currentMagnitudeSurvey
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1
        AND t.transientBucketId=thisID;




UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        a.transientBucketId,
            a.observationDate AS classificationDate,
            a.spectralType AS recentClassification,
            a.classificationWRTMax AS classificationWRTMax,
            a.classificationPhase AS classificationPhase,
            a.reducer AS classificationAddedBy,
            a.dateCreated AS classificationAddedDate,
            a.transientRedshift AS best_redshift,
            a.survey AS classificationSurvey
    FROM
        transientBucket a
    JOIN (SELECT 
        *
    FROM
        (SELECT 
        MAX(observationDate) AS maxval, transientBucketId
    FROM
        transientBucket
    WHERE
		transientBucketId=thisID and
        spectralType IS NOT NULL
            AND replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
				transientBucketId=thisID and
                updateNeeded = 1)
    GROUP BY transientBucketId) AS c
    ORDER BY transientBucketId) AS b ON a.transientBucketId = b.transientBucketId
        AND a.observationDate = b.maxval
    WHERE
        spectralType IS NOT NULL
            AND a.replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND a.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS d
    ORDER BY transientBucketId) t 
SET 
    s.classificationDate = t.classificationDate,
    s.recentClassification = t.recentClassification,
    s.classificationWRTMax = t.classificationWRTMax,
    s.classificationPhase = t.classificationPhase,
    s.classificationAddedBy = t.classificationAddedBy,
    s.classificationAddedDate = t.classificationAddedDate,
    s.classificationSurvey = t.classificationSurvey,
    s.best_redshift = t.best_redshift
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1
        AND t.transientBucketId=thisID;

        

UPDATE transientBucketSummaries s,
    sherlock_crossmatches c 
SET 
    s.sherlockClassification = c.association_type,
    s.separationArcsec = c.separationArcsec,
    s.distanceMpc = IF(c.direct_distance,
        c.direct_distance,
        c.distance),
    s.best_redshift = IF(s.best_redshift IS NULL,
        c.z,
        s.best_redshift),
    s.host_redshift = IF(c.z AND c.z != s.host_redshift,
        c.z,
        s.host_redshift)
WHERE
	
    c.rank = 1
        AND s.transientBucketId = c.transient_object_id
        AND c.transient_object_id IN (SELECT 
            *
        FROM
            (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1) AS a)
        AND s.updateNeeded = 1
        AND s.transientBucketId=thisID;


UPDATE transientBucketSummaries 
SET 
    absolutePeakMagnitude = peakMagnitude - (5 * LOG10(distanceMpc * 1000000) - 5)
WHERE
    distanceMpc IS NOT NULL
        AND peakMagnitude IS NOT NULL
        AND peakMagnitude < 24.0
        AND absolutePeakMagnitude IS NULL
        AND transientBucketId=thisID;
    
    

UPDATE transientBucketSummaries s 
SET 
    updateNeeded = 2
WHERE
    updateNeeded = 1
    AND transientBucketId=thisID;


UPDATE transientBucketSummaries t,
        pesstoObjects p 
    SET 
        marshallWorkflowLocation = 'archive'
    WHERE
        t.mastername LIKE 'ZTF%%'
            AND (t.currentMagnitude > 20.0
            OR ABS(t.gLat) < 10)
            AND p.transientBucketId = t.transientBucketId
            AND marshallWorkflowLocation = "inbox"
            AND t.transientBucketId=thisID;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_tns_tables` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_tns_tables`()
BEGIN
-- update tns_spectra set ingested  = 1 where survey like "%PESSTO%";
update tns_spectra set TNSName = concat("AT",TNSId) where specType not like "%SN%" and TNSName is null;
update tns_spectra set TNSName = concat("SN",TNSId) where specType  like "%SN%" and TNSName is null;
update tns_spectra p, tns_sources s set p.raDeg = s.raDeg, p.decDeg = s.decDeg where p.TNSId=s.TNSId and s.raDeg is not null;
update tns_photometry p, tns_sources s set p.raDeg = s.raDeg, p.decDeg = s.decDeg where p.TNSId=s.TNSId and s.raDeg is not null;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_transientbucketsummaries` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_transientbucketsummaries`()
BEGIN

-- MOVE CLASSIFIED SOURCES OUT OF THE INBOX & CLASSIFICATION QUEUE
UPDATE pesstoObjects p,
    transientBucketSummaries t 
SET 
    p.classifiedFlag = 1
WHERE
    t.recentClassification IS NOT NULL
        AND p.classifiedFlag != 1
        AND p.transientBucketId = t.transientBucketId;
                        
-- INSERT HISTORY LOG
insert into transients_history_logs  (transientBucketId, log) SELECT 
                pesstoObjectsId, CONCAT("moved from ",marshallWorkflowLocation, " to 'review for followup' by marshall code")
            FROM
                pesstoObjects
            WHERE
                marshallWorkflowLocation in ('pending classification', 'inbox')
                    AND classifiedFlag = 1;

-- MOVE CLASSIFIED SOURCES
UPDATE pesstoObjects 
SET 
    marshallWorkflowLocation = 'review for followup',
    snoozed = 0
WHERE
    marshallWorkflowLocation IN ('pending classification' , 'inbox')
        AND classifiedFlag = 1;
                        
                    
-- ADD NEW SOURCES TO PESSTOOBJECTS -- NEED TO MERGE PESSTOOBJECTS INTO transientBucketSummaries TABLE
INSERT INTO pesstoObjects (
		pesstoObjectsId,
		transientBucketId,
		classifiedFlag,
		marshallWorkflowLocation,
		alertWorkflowLocation,
		publicStatus,
		dateAdded,
		dateLastModified)  
	SELECT 
		transientBucketId, transientBucketId, 0, "Inbox", 'Pending Classification', 1, now(), now()
	FROM
		transientBucket
	WHERE
		transientBucketId NOT IN (SELECT 
				transientBucketId
			FROM
				pesstoObjects) AND transientBucketId > 0 and masterIDFlag = 1;

-- ADD NEW TRANSIENTS TO THE transientBucketSummaries TABLE
INSERT ignore INTO transientBucketSummaries (transientBucketId)
select distinct transientBucketId from transientBucket where replacedByRowId = 0 and transientBucketId != 0 and masterIDFlag = 1 and dateLastModified > DATE_SUB(curdate(), INTERVAL 1 WEEK);

-- SET UPDATE FLAG
UPDATE transientBucketSummaries 
SET 
    updateNeeded = 1
WHERE
    transientBucketId IN (SELECT 
            *
        FROM
            (SELECT 
                a.transientBucketId
            FROM
                transientBucketSummaries a, (SELECT 
                transientBucketId, MAX(dateLastModified) AS dateLastModified
            FROM
                transientBucket
            WHERE
                dateLastModified > DATE_SUB(CURDATE(), INTERVAL 1 WEEK)
            GROUP BY transientBucketId) b
            WHERE
                a.transientBucketId = b.transientBucketId
                    AND a.dateLastModified < b.dateLastModified
                    AND a.updateNeeded NOT IN (1 , 2)) c);	

-- UPDATE MASTER TRANSIENTS NAMES & DISCOVERY SURVEY (EPOCH OF FIRST DETECTION)
UPDATE transientBucketSummaries s,
    transientBucket t 
SET 
    s.masterName = t.name,
    s.surveyObjectUrl = t.surveyObjectUrl
WHERE
    masterIdFlag = 1 AND replacedByRowId = 0
        AND s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1;
       
-- UPDATE SURVEYURL IF MISSING
UPDATE transientBucket t,
    transientBucketSummaries s 
SET 
    s.surveyObjectUrl = t.surveyObjectUrl
WHERE
    t.surveyObjectUrl IS NOT NULL
        AND s.surveyObjectUrl IS NULL
        AND t.transientBucketId = s.transientBucketId
        AND t.surveyObjectUrl NOT LIKE '%%astronomerstelegram%%'
        AND t.surveyObjectUrl NOT LIKE '%%roche%%'
        AND replacedByRowId = 0
        AND masterIDFlag = 1;

UPDATE transientBucket t,
    transientBucketSummaries s 
SET 
    s.surveyObjectUrl = t.surveyObjectUrl
WHERE
    t.surveyObjectUrl IS NOT NULL
        AND s.surveyObjectUrl IS NULL
        AND t.transientBucketId = s.transientBucketId
        AND t.surveyObjectUrl NOT LIKE '%%astronomerstelegram%%'
        AND t.surveyObjectUrl NOT LIKE '%%roche%%'
        AND replacedByRowId = 0;
      
-- ADDED BY WHICH USER     
UPDATE transientBucketSummaries s,
    transientBucket t 
SET 
    s.objectAddedToMarshallBy = t.reducer
WHERE
    t.reducer IS NOT NULL
        AND t.spectralType IS NULL
        AND t.transientBucketId = s.transientBucketId
        AND replacedByRowId = 0
        AND s.updateNeeded = 1;
      
-- UPDATE OBJECT'S METADATA
UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        transientBucketId,
            AVG(raDeg) AS raDeg,
            AVG(decDeg) AS decDeg,
            MIN(dateCreated) AS dateAdded,
            MIN(magnitude) AS peakMagnitude
    FROM
        transientBucket
    WHERE
        replacedByRowId = 0 AND limitingMag = 0
            AND magnitude IS NOT NULL
            AND magnitude > 0.0
            AND magnitude < 25.0
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS a
    ORDER BY transientBucketId) t 
SET 
    s.raDeg = t.raDeg,
    s.decDeg = t.decDeg,
    s.dateAdded = t.dateAdded,
    s.peakMagnitude = t.peakMagnitude
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1;

-- NULL RA/DEC
UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        transientBucketId,
            AVG(raDeg) AS raDeg,
            AVG(decDeg) AS decDeg
    FROM
        transientBucket
    WHERE
        replacedByRowId = 0
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                raDeg IS NULL AND updateNeeded = 1)
    GROUP BY transientBucketId) AS a
    ORDER BY transientBucketId) t 
SET 
    s.raDeg = t.raDeg,
    s.decDeg = t.decDeg
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1;

UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        transientBucketId, MIN(hostRedshift) AS host_redshift
    FROM
        transientBucket
    WHERE
        replacedByRowId = 0
            AND hostRedshift IS NOT NULL
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS a
    ORDER BY transientBucketId) t 
SET 
    s.host_redshift = t.host_redshift
WHERE
    s.transientBucketId = t.transientBucketId
        AND updateNeeded = 1;

-- UPDATE EARLIEST DETECTION INFORMATION
UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        a.transientBucketId,
            a.observationDate AS earliestDetection,
            a.magnitude AS earliestMagnitude,
            a.filter AS earliestMagnitudeFilter,
            a.survey AS earliestMagnitudeSurvey
    FROM
        transientBucket a
    JOIN (SELECT 
        MIN(observationDate) AS minval, transientBucketId
    FROM
        transientBucket
    WHERE
        magnitude IS NOT NULL
            AND limitingMag = 0
            AND replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS b ON a.transientBucketId = b.transientBucketId
        AND a.observationDate = b.minval
    WHERE
        a.limitingMag = 0
            AND a.replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND a.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS c
    ORDER BY transientBucketId) t 
SET 
    s.earliestDetection = t.earliestDetection,
    s.earliestMagnitude = t.earliestMagnitude,
    s.earliestMagnitudeFilter = t.earliestMagnitudeFilter,
    s.earliestMagnitudeSurvey = t.earliestMagnitudeSurvey
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1;

-- LAST NON-DETECTION
UPDATE transientBucketSummaries a,
    (SELECT 
        *
    FROM
        (SELECT 
        s.transientBucketId,
            MAX(t.lastNonDetectionDate) AS lastNonDetectionDate
    FROM
        transientBucket t, transientBucketSummaries s
    WHERE
        t.lastNonDetectionDate < s.earliestDetection
            AND s.transientBucketId = t.transientBucketId
            AND replacedByRowId = 0
            AND t.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY s.transientBucketId) AS c
    ORDER BY transientBucketId) b 
SET 
    a.lastNonDetectionDate = b.lastNonDetectionDate
WHERE
    a.transientBucketId = b.transientBucketId
        AND a.updateNeeded = 1;
    

UPDATE transientBucketSummaries a,
    (SELECT 
        *
    FROM
        (SELECT 
        s.transientBucketId,
            MAX(t.observationDate) AS lastNonDetectionDate
    FROM
        transientBucket t, transientBucketSummaries s
    WHERE
        t.observationDate < s.earliestDetection
            AND (t.observationDate > s.lastNonDetectionDate
            OR s.lastNonDetectionDate IS NULL)
            AND s.transientBucketId = t.transientBucketId
            AND replacedByRowId = 0
            AND t.limitingMag = 1
            AND t.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY s.transientBucketId) AS a
    ORDER BY transientBucketId) b 
SET 
    a.lastNonDetectionDate = b.lastNonDetectionDate
WHERE
    a.transientBucketId = b.transientBucketId
        AND a.updateNeeded = 1;

-- UPDATE CURRENT MAGNITUDE INFORMATION
UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        a.transientBucketId,
            a.observationDate AS currentMagnitudeDate,
            a.magnitude AS currentMagnitude,
            a.filter AS currentMagnitudeFilter,
            a.survey AS currentMagnitudeSurvey
    FROM
        transientBucket a
    JOIN (SELECT 
        *
    FROM
        (SELECT 
        MAX(observationDate) AS maxval, transientBucketId
    FROM
        transientBucket
    WHERE
        magnitude IS NOT NULL
            AND limitingMag = 0
            AND replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS d
    ORDER BY transientBucketId) AS b ON a.transientBucketId = b.transientBucketId
        AND a.observationDate = b.maxval
    WHERE
        a.limitingMag = 0
            AND a.replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND a.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)
    GROUP BY transientBucketId) AS c
    ORDER BY transientBucketId) t 
SET 
    s.currentMagnitudeDate = t.currentMagnitudeDate,
    s.currentMagnitude = t.currentMagnitude,
    s.currentMagnitudeFilter = t.currentMagnitudeFilter,
    s.currentMagnitudeSurvey = t.currentMagnitudeSurvey
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1;



-- UPDATE LATEST CLASSIFICATION INFORMATION
UPDATE transientBucketSummaries s,
    (SELECT 
        *
    FROM
        (SELECT 
        a.transientBucketId,
            a.observationDate AS classificationDate,
            a.spectralType AS recentClassification,
            a.classificationWRTMax AS classificationWRTMax,
            a.classificationPhase AS classificationPhase,
            a.reducer AS classificationAddedBy,
            a.dateCreated AS classificationAddedDate,
            a.transientRedshift AS best_redshift,
            a.survey as classificationSurvey
    FROM
        transientBucket a
    JOIN (SELECT 
        *
    FROM
        (SELECT 
        MAX(observationDate) AS maxval,max(dateCreated) as addval, transientBucketId
    FROM
        transientBucket
    WHERE
        spectralType IS NOT NULL
            AND replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
               updateNeeded = 1)
    GROUP BY transientBucketId) AS c
    ORDER BY transientBucketId) AS b ON a.transientBucketId = b.transientBucketId
        AND a.observationDate = b.maxval
        AND a.dateCreated = b.addval
    WHERE
        spectralType IS NOT NULL
            AND a.replacedByRowId = 0
            AND observationDate IS NOT NULL
            AND a.transientBucketId IN (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1)) AS d
    ORDER BY transientBucketId) t 
SET 
    s.classificationDate = t.classificationDate,
    s.recentClassification = t.recentClassification,
    s.classificationWRTMax = t.classificationWRTMax,
    s.classificationPhase = t.classificationPhase,
    s.classificationAddedBy = t.classificationAddedBy,
    s.classificationAddedDate = t.classificationAddedDate,
    s.best_redshift = t.best_redshift,
    s.classificationSurvey = t.classificationSurvey
WHERE
    s.transientBucketId = t.transientBucketId
        AND s.updateNeeded = 1;

        
-- UPDATE CONTEXT INFO FROM SHERLOCK 
UPDATE transientBucketSummaries s,
    sherlock_crossmatches c 
SET 
    s.sherlockClassification = c.association_type,
    s.separationArcsec = c.separationArcsec,
    s.distanceMpc = IF(c.direct_distance,
        c.direct_distance,
        c.distance),
    s.best_redshift = IF(s.best_redshift IS NULL,
        c.z,
        s.best_redshift),
    s.host_redshift = IF(c.z AND c.z != s.host_redshift,
        c.z,
        s.host_redshift)
WHERE
    c.rank = 1
        AND s.transientBucketId = c.transient_object_id
        AND c.transient_object_id IN (SELECT 
            *
        FROM
            (SELECT 
                transientBucketId
            FROM
                transientBucketSummaries
            WHERE
                updateNeeded = 1) AS a)
        AND s.updateNeeded = 1;

-- UPDATE ABS PEAK MAG
UPDATE transientBucketSummaries 
SET 
    absolutePeakMagnitude = peakMagnitude - (5 * LOG10(distanceMpc * 1000000) - 5)
WHERE
    distanceMpc IS NOT NULL
        AND peakMagnitude IS NOT NULL
        AND peakMagnitude < 24.0
        AND absolutePeakMagnitude IS NULL;
    
    
-- KEEP FLAG SET FOR PYTHON UPDATES
UPDATE transientBucketSummaries s 
SET 
    updateNeeded = 2
WHERE
    updateNeeded = 1; 

-- ARCHIVE LOW PRIORITY ZTF TARGETS
UPDATE transientBucketSummaries t,
        pesstoObjects p 
    SET 
        marshallWorkflowLocation = 'archive'
    WHERE
        t.mastername LIKE 'ZTF%%'
            AND (t.currentMagnitude > 20.0
            OR ABS(t.gLat) < 10)
            AND p.transientBucketId = t.transientBucketId
            AND marshallWorkflowLocation = "inbox";


END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_transientBucket_atlas_sources` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_transientBucket_atlas_sources`()
BEGIN
	-- TRANSFER IMAGE URLS TO FP
UPDATE transientBucket a
        INNER JOIN
    transientBucket b ON a.transientBucketId = b.transientBucketId 
SET 
    a.targetImageUrl = b.targetImageUrl,
    a.referenceImageUrl = b.referenceImageUrl,
    a.subtractedImageUrl = b.subtractedImageUrl
WHERE
    a.survey = 'ATLAS FP'
        AND a.targetImageUrl IS NULL
        AND a.dateCreated > DATE_SUB(CURDATE(), INTERVAL 3 WEEK)
        AND b.survey = 'atlas'
        AND a.targetImageUrl IS NOT NULL
        AND b.dateCreated > DATE_SUB(CURDATE(), INTERVAL 4 WEEK);
                
-- TRANSFER THE OBJECT'S SURVEY URL FROM NON-FORCED TO FORCED PHOT
UPDATE transientBucket a
        INNER JOIN
    transientBucket b ON a.transientBucketId = b.transientBucketId 
SET 
    a.surveyObjectUrl = b.surveyObjectUrl
WHERE
    a.survey = 'ATLAS FP'
        AND (a.surveyObjectUrl IS NULL OR a.surveyObjectUrl NOT LIKE '%atlas4%')
        AND a.dateCreated > DATE_SUB(CURDATE(), INTERVAL 3 WEEK)
        AND b.survey = 'atlas'
        AND b.dateDeleted IS NULL
        AND a.targetImageUrl IS NOT NULL
        AND b.dateCreated > DATE_SUB(CURDATE(), INTERVAL 4 WEEK);
                
-- SWITCH THE MASTER IDs
update transientBucket set masterIDFlag = 1 where primaryKeyId in (select * from (
SELECT
    min(b.primaryKeyId) as newMasterPrimaryId
FROM
    transientBucket a
INNER JOIN
	transientBucket b on a.transientBucketId=b.transientBucketId
WHERE
    a.survey = 'atlas' AND a.masterIDFlag = 1
        AND a.surveyObjectURL NOT LIKE '%wis-tns%'
        AND a.dateDeleted IS NULL and
	b.survey = 'ATLAS FP' group by b.transientBucketId) as c) and dateCreated > DATE_SUB(curdate(), INTERVAL 3 week);
    
update 
    transientBucket a
INNER JOIN
	transientBucket b on a.transientBucketId=b.transientBucketId
set b.masterIDFlag = 0
WHERE
    a.survey = 'ATLAS FP' AND a.masterIDFlag = 1
        AND a.dateDeleted IS NULL and b.survey != 'ATLAS FP' 
	 and a.dateCreated > DATE_SUB(curdate(), INTERVAL 3 week) and b.dateCreated > DATE_SUB(curdate(), INTERVAL 3 week) and
	b.masterIDFlag = 1;   
                    
	-- FINALLY I CAN SET THE `DATEDELETED` FLAG IN THE TRANSIENTBUCKET TABLE
update transientBucket a
INNER JOIN
	transientBucket b on a.transientBucketId=b.transientBucketId
set b.dateDeleted = NOW(),
    b.replacedbyRowId = - 1
WHERE
    a.survey = 'ATLAS FP' AND a.masterIDFlag = 1
        AND a.dateDeleted IS NULL and b.survey = 'atlas' and b.surveyObjectURL NOT LIKE '%%wis-tns%%' and b.replacedbyRowId is null
        and a.dateCreated > DATE_SUB(curdate(), INTERVAL 3 week) and b.dateCreated > DATE_SUB(curdate(), INTERVAL 3 week); 
                        
	-- UPDATE ENTRIES WITH NO SURVEY URL
UPDATE transientBucket 
SET 
    surveyObjectUrl = CONCAT('https://star.pst.qub.ac.uk/sne/atlas4/candidate/',
            SUBSTRING_INDEX(SUBSTRING_INDEX(referenceImageUrl, '_', 2),
                    '/',
                    - 1))
WHERE
    survey = 'ATLAS FP'
        AND surveyObjectUrl IS NULL
        AND referenceImageUrl IS NOT NULL;
                
	-- A FIX TO IMPORT THE ATLAS URLS INTO THE TRANSIENT BUCKET
UPDATE transientBucket t,
    fs_atlas a 
SET 
    t.surveyObjectUrl = a.objectURL
WHERE
    t.name = a.candidateId
        AND t.surveyObjectUrl IS NULL
        AND a.objectURL IS NOT NULL
        AND a.dateCreated > DATE_SUB(CURDATE(), INTERVAL 3 WEEK)
        AND t.dateCreated > DATE_SUB(CURDATE(), INTERVAL 3 WEEK); 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_transientbucket_observation_dates` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_transientbucket_observation_dates`()
BEGIN
	UPDATE transientBucket set observationMJD = null where observationMJD = 0;
UPDATE transientBucket set observationMJD = observationMJD - 2400000.5 where observationMJD > 245000;

UPDATE ignore transientBucket 
SET 
    observationDate = FROM_UNIXTIME((observationMJD + 678941) * (3600 * 24) - TO_SECONDS('1970-01-01 00:00:00') + TO_SECONDS(UTC_TIMESTAMP()) - TO_SECONDS(CURRENT_TIMESTAMP()))
WHERE
    observationMJD IS NOT NULL and observationDate  is null limit 50000;

UPDATE ignore transientBucket 
SET 
    observationMjd = TO_SECONDS(observationDate) / (3600 * 24) - 678941
WHERE
    observationMjd IS NULL
        AND observationDate IS NOT NULL limit 50000;
        
DELETE FROM `transientbucket` WHERE observationMjd is null and dateCreated < DATE_SUB(curdate(), INTERVAL 3 hour);

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_transients_with_no_masteridflag` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_transients_with_no_masteridflag`()
BEGIN
-- IF OBJECT HAS MORE THAN ONE MASTERID THEN SET MASTERID TO ZERO
update  transientBucket A
INNER JOIN
(select transientBucketId from transientBucket
    WHERE
        masterIDFlag = 1
        and replacedByRowId = 0
GROUP BY transientBucketId having count(*) > 1) B on A.transientBucketId=B.transientBucketId set A.masterIDFlag = 0 where A.masterIDFlag=1;

-- MAKE SURE MASTERID NOT IN REPLACED ROWS
update transientBucket set masterIDFlag  = 0 where masterIDFlag  = 1 and replacedByRowId != 0;

-- UPDATE TRANSIENTBUCKET AND TRANSIENTBUCKETSUMMARIES TO SET MASTERID = 1 FOR MIN(primaryKeyId) IF NO MASTERID
update transientBucket c
INNER JOIN
(SELECT 
    primaryKeyId
FROM
    transientBucket a
        LEFT JOIN
    (SELECT 
        transientBucketId
    FROM
        transientBucket
    WHERE
        masterIDFlag = 1 AND replacedByRowId = 0
    GROUP BY transientBucketId) b ON (a.transientBucketId = b.transientBucketId)
WHERE
    b.transientBucketId IS NULL and a.replacedByRowId = 0 group by a.transientBucketId) d on c.primaryKeyId=d.primaryKeyId
    set c.masterIdFlag = 1;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_transient_akas` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE  PROCEDURE `update_transient_akas`()
BEGIN
-- UPDATE THE TNS RECORDS
update ignore
    transientBucket t,
    tns_spectra s,
    pesstoObjects p
set t.name = TNSName
WHERE
	s.dateCreated > DATE_SUB(CURDATE(), INTERVAL 3 DAY) AND 
    p.classifiedFlag = 1
        AND p.transientBucketId = t.transientBucketId
        AND t.transientBucketId = s.transientBucketId
        AND t.name LIKE 'AT2%'
        AND TNSName LIKE 'SN%';
update ignore
    transientBucket t,
    tns_spectra s,
    pesstoObjects p
set t.name = TNSName
WHERE
	s.dateCreated > DATE_SUB(CURDATE(), INTERVAL 3 DAY) AND 
    p.classifiedFlag = 1
        AND p.transientBucketId = t.transientBucketId
        AND t.name LIKE 'AT2%'
        AND t.name = replace(TNSName, 'SN', 'AT')
        AND TNSName LIKE 'SN%' and s.survey like "%PESSTO%";
        
-- CLEAN UP CLASSIFIED AT NAMES
DELETE FROM marshall_transient_akas 
WHERE
    primaryId IN (SELECT 
        *
    FROM
        (SELECT 
            a.primaryId
        FROM
            marshall_transient_akas a, (SELECT 
            *
        FROM
            marshall_transient_akas
        
        WHERE
            name LIKE 'SN2%') b
        
        WHERE
            a.name LIKE 'AT2%'
            AND a.transientBucketId = b.transientBucketId
            AND a.name = REPLACE(b.name, 'SN', 'AT')) AS c);
        
-- ADD NEW ROWS TO AKA TABLE
INSERT IGNORE INTO marshall_transient_akas (transientBucketId, name)
select distinct transientBucketId, name from transientBucket where name not like "atel_%" and dateCreated > DATE_SUB(curdate(), INTERVAL 3 WEEK) order by transientBucketId;

-- UPDATE ATLAS URLS
update
        fs_atlas_forced_phot a, transientBucket t
set t.surveyObjectUrl=CONCAT('https://star.pst.qub.ac.uk/sne/atlas4/candidate/', a.atlas_object_id)
WHERE
    t.surveyObjectUrl IS NULL
        AND t.name = a.atlas_designation
        AND a.atlas_designation IN (SELECT 
            name
        FROM
            marshall_transient_akas
        WHERE
            url IS NULL and name like "ATLAS%");

update marshall_transient_akas set url = concat("https://lasair.roe.ac.uk/object/",name) where name like "ZTF%" and url is null;
update marshall_transient_akas set url = concat("https://wis-tns.weizmann.ac.il/object/",name) where (name like "AT20%" or name like "AT19%" or name like "SN19%" or name like "SN20%") and url is null;
update marshall_transient_akas a, (select distinct name, surveyObjectUrl from transientBucket where name like "LSQ%" and surveyObjectUrl is not null and surveyObjectUrl  like "%nersc%") t set a.url = t.surveyObjectUrl where a.name=t.name and a.url is null;
update marshall_transient_akas a, (select distinct name, surveyObjectUrl from transientBucket where (name like "PS1%" or name like "PS2%") and surveyObjectUrl is not null and surveyObjectUrl like "%star.pst%") t set a.url = t.surveyObjectUrl where a.name=t.name and a.url is null;
update marshall_transient_akas a, (select distinct name, surveyObjectUrl from transientBucket where name like "ATLAS%" and surveyObjectUrl is not null and surveyObjectUrl like "%star.pst%") t set a.url = t.surveyObjectUrl where a.name=t.name and a.url is null;
update marshall_transient_akas a, (select distinct name, surveyObjectUrl from transientBucket where (name like "CSS%" or name like "MLS%" or name like "SSS%") and surveyObjectUrl is not null and surveyObjectUrl like "%nesssi%") t set a.url = t.surveyObjectUrl where a.name=t.name and a.url is null;
update marshall_transient_akas a, (select distinct name, surveyObjectUrl from transientBucket where name like "PSN%" and surveyObjectUrl is not null and surveyObjectUrl like "%cbat%") t set a.url = t.surveyObjectUrl where a.name=t.name and a.url is null;
update marshall_transient_akas set url = concat("http://gsaweb.ast.cam.ac.uk/alerts/alert/",name) where name like "Gaia%" and url is null;
update marshall_transient_akas set url = "http://www.astronomy.ohio-state.edu/asassn/sn_list.html" where (name like "ASASSN-1%" and name not like "ASASSN-19%") and url is null;
update marshall_transient_akas set url = "http://ogle.astrouw.edu.pl/ogle4/transients/" where name like "OGLE%" and url is null;

-- UPDATE ASSASN URLs
UPDATE marshall_transient_akas c,
    (SELECT 
        a.name,
            REPLACE(b.name, 'AT', 'http://asassn.china-vo.org/public/lc?dir=') AS url
    FROM
        marshall_transient_akas a
    INNER JOIN marshall_transient_akas b ON a.transientBucketId = b.transientBucketId
    WHERE
        b.name LIKE 'AT2%'
            AND (a.name LIKE 'ASASSN-19%'
            OR a.name LIKE 'ASASSN-2%')
            AND a.url IS NULL
            AND LENGTH(b.name) > 8
            AND b.name NOT LIKE '%19a%'
            AND b.name NOT LIKE '%19b%'
            AND b.name LIKE '%19%') d 
SET 
    c.url = d.url
WHERE
    c.name = d.name;
    
-- UPDATE ASSASN URLs
UPDATE marshall_transient_akas c,
    (SELECT 
        a.name,
            REPLACE(b.name, 'SN', 'http://asassn.china-vo.org/public/lc?dir=') AS url
    FROM
        marshall_transient_akas a
    INNER JOIN marshall_transient_akas b ON a.transientBucketId = b.transientBucketId
    WHERE
        b.name LIKE 'SN2%'
            AND (a.name LIKE 'ASASSN-19%'
            OR a.name LIKE 'ASASSN-2%')
            AND a.url IS NULL
            AND LENGTH(b.name) > 8
            AND b.name NOT LIKE '%19a%'
            AND b.name NOT LIKE '%19b%'
            AND b.name LIKE '%19%') d 
SET 
    c.url = d.url
WHERE
    c.name = d.name;

-- UPDATE TNS URLS
update marshall_transient_akas set url = replace(url,"object/AT","object/") where url like "%object/AT%";
update marshall_transient_akas set url = replace(url,"object/SN","object/") where url like "%object/SN%";

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `_subview_object_akas`
--

/*!50001 DROP TABLE IF EXISTS `_subview_object_akas`*/;
/*!50001 DROP VIEW IF EXISTS `_subview_object_akas`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `_subview_object_akas` AS select 1 AS `transientBucketId`,1 AS `primaryKeyId`,1 AS `name`,1 AS `survey`,1 AS `surveyObjectUrl`,1 AS `referenceImageUrl`,1 AS `targetImageUrl`,1 AS `subtractedImageUrl`,1 AS `tripletImageUrl`,1 AS `finderImageUrl` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_fs_crts_css_summary`
--

/*!50001 DROP TABLE IF EXISTS `view_fs_crts_css_summary`*/;
/*!50001 DROP VIEW IF EXISTS `view_fs_crts_css_summary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_fs_crts_css_summary` AS select `fs_crts_css`.`primaryId` AS `primaryId`,`fs_crts_css`.`circularUrl` AS `circularUrl`,`fs_crts_css`.`comment` AS `comment`,`fs_crts_css`.`commentIngested` AS `commentIngested`,`fs_crts_css`.`dateCreated` AS `dateCreated`,`fs_crts_css`.`dateLastModified` AS `dateLastModified`,`fs_crts_css`.`dateLastRead` AS `dateLastRead`,`fs_crts_css`.`decDeg` AS `decDeg`,`fs_crts_css`.`filter` AS `filter`,`fs_crts_css`.`finderChartUrl` AS `finderChartUrl`,`fs_crts_css`.`finderChartWebpage` AS `finderChartWebpage`,`fs_crts_css`.`imagesUrl` AS `imagesUrl`,`fs_crts_css`.`ingested` AS `ingested`,`fs_crts_css`.`lightcurveUrl` AS `lightcurveUrl`,`fs_crts_css`.`mag` AS `mag`,`fs_crts_css`.`name` AS `name`,`fs_crts_css`.`observationDate` AS `observationDate`,`fs_crts_css`.`observationMJD` AS `observationMJD`,`fs_crts_css`.`raDeg` AS `raDeg`,`fs_crts_css`.`summaryRow` AS `summaryRow`,`fs_crts_css`.`survey` AS `survey`,`fs_crts_css`.`surveyObjectUrl` AS `surveyObjectUrl`,`fs_crts_css`.`targetImageUrl` AS `targetImageUrl`,`fs_crts_css`.`transientTypePrediction` AS `transientTypePrediction`,`fs_crts_css`.`uniqueId` AS `uniqueId`,`fs_crts_css`.`htm16ID` AS `htm16ID`,`fs_crts_css`.`magErr` AS `magErr`,`fs_crts_css`.`lastNonDetectionDate` AS `lastNonDetectionDate`,`fs_crts_css`.`lastNonDetectionMJD` AS `lastNonDetectionMJD` from `fs_crts_css` where `fs_crts_css`.`summaryRow` is true */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_fs_crts_mls_summary`
--

/*!50001 DROP TABLE IF EXISTS `view_fs_crts_mls_summary`*/;
/*!50001 DROP VIEW IF EXISTS `view_fs_crts_mls_summary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_fs_crts_mls_summary` AS select `fs_crts_mls`.`primaryId` AS `primaryId`,`fs_crts_mls`.`circularUrl` AS `circularUrl`,`fs_crts_mls`.`comment` AS `comment`,`fs_crts_mls`.`commentIngested` AS `commentIngested`,`fs_crts_mls`.`dateCreated` AS `dateCreated`,`fs_crts_mls`.`dateLastModified` AS `dateLastModified`,`fs_crts_mls`.`dateLastRead` AS `dateLastRead`,`fs_crts_mls`.`decDeg` AS `decDeg`,`fs_crts_mls`.`filter` AS `filter`,`fs_crts_mls`.`finderChartUrl` AS `finderChartUrl`,`fs_crts_mls`.`finderChartWebpage` AS `finderChartWebpage`,`fs_crts_mls`.`imagesUrl` AS `imagesUrl`,`fs_crts_mls`.`ingested` AS `ingested`,`fs_crts_mls`.`lightcurveUrl` AS `lightcurveUrl`,`fs_crts_mls`.`mag` AS `mag`,`fs_crts_mls`.`name` AS `name`,`fs_crts_mls`.`observationDate` AS `observationDate`,`fs_crts_mls`.`observationMJD` AS `observationMJD`,`fs_crts_mls`.`raDeg` AS `raDeg`,`fs_crts_mls`.`summaryRow` AS `summaryRow`,`fs_crts_mls`.`survey` AS `survey`,`fs_crts_mls`.`surveyObjectUrl` AS `surveyObjectUrl`,`fs_crts_mls`.`targetImageUrl` AS `targetImageUrl`,`fs_crts_mls`.`transientTypePrediction` AS `transientTypePrediction`,`fs_crts_mls`.`uniqueId` AS `uniqueId`,`fs_crts_mls`.`htm16ID` AS `htm16ID`,`fs_crts_mls`.`magErr` AS `magErr`,`fs_crts_mls`.`lastNonDetectionDate` AS `lastNonDetectionDate`,`fs_crts_mls`.`lastNonDetectionMJD` AS `lastNonDetectionMJD` from `fs_crts_mls` where `fs_crts_mls`.`summaryRow` is true */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_fs_crts_sss_summary`
--

/*!50001 DROP TABLE IF EXISTS `view_fs_crts_sss_summary`*/;
/*!50001 DROP VIEW IF EXISTS `view_fs_crts_sss_summary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_fs_crts_sss_summary` AS select `fs_crts_sss`.`primaryId` AS `primaryId`,`fs_crts_sss`.`circularUrl` AS `circularUrl`,`fs_crts_sss`.`comment` AS `comment`,`fs_crts_sss`.`commentIngested` AS `commentIngested`,`fs_crts_sss`.`dateCreated` AS `dateCreated`,`fs_crts_sss`.`dateLastModified` AS `dateLastModified`,`fs_crts_sss`.`dateLastRead` AS `dateLastRead`,`fs_crts_sss`.`decDeg` AS `decDeg`,`fs_crts_sss`.`filter` AS `filter`,`fs_crts_sss`.`finderChartUrl` AS `finderChartUrl`,`fs_crts_sss`.`finderChartWebpage` AS `finderChartWebpage`,`fs_crts_sss`.`imagesUrl` AS `imagesUrl`,`fs_crts_sss`.`ingested` AS `ingested`,`fs_crts_sss`.`lightcurveUrl` AS `lightcurveUrl`,`fs_crts_sss`.`mag` AS `mag`,`fs_crts_sss`.`name` AS `name`,`fs_crts_sss`.`observationDate` AS `observationDate`,`fs_crts_sss`.`observationMJD` AS `observationMJD`,`fs_crts_sss`.`raDeg` AS `raDeg`,`fs_crts_sss`.`summaryRow` AS `summaryRow`,`fs_crts_sss`.`survey` AS `survey`,`fs_crts_sss`.`surveyObjectUrl` AS `surveyObjectUrl`,`fs_crts_sss`.`targetImageUrl` AS `targetImageUrl`,`fs_crts_sss`.`transientTypePrediction` AS `transientTypePrediction`,`fs_crts_sss`.`uniqueId` AS `uniqueId`,`fs_crts_sss`.`htm16ID` AS `htm16ID`,`fs_crts_sss`.`magErr` AS `magErr`,`fs_crts_sss`.`lastNonDetectionDate` AS `lastNonDetectionDate`,`fs_crts_sss`.`lastNonDetectionMJD` AS `lastNonDetectionMJD` from `fs_crts_sss` where `fs_crts_sss`.`summaryRow` is true */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_fs_ogle_summary`
--

/*!50001 DROP TABLE IF EXISTS `view_fs_ogle_summary`*/;
/*!50001 DROP VIEW IF EXISTS `view_fs_ogle_summary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_fs_ogle_summary` AS select `fs_ogle`.`primaryId` AS `primaryId`,`fs_ogle`.`dateCreated` AS `dateCreated`,`fs_ogle`.`dateLastModified` AS `dateLastModified`,`fs_ogle`.`dateLastRead` AS `dateLastRead`,`fs_ogle`.`decDeg` AS `decDeg`,`fs_ogle`.`filter` AS `filter`,`fs_ogle`.`ingested` AS `ingested`,`fs_ogle`.`lastNonDetectionDate` AS `lastNonDetectionDate`,`fs_ogle`.`lastNonDetectionMJD` AS `lastNonDetectionMJD`,`fs_ogle`.`lightcurveUrl` AS `lightcurveUrl`,`fs_ogle`.`mag` AS `mag`,`fs_ogle`.`name` AS `name`,`fs_ogle`.`observationDate` AS `observationDate`,`fs_ogle`.`observationMJD` AS `observationMJD`,`fs_ogle`.`raDeg` AS `raDeg`,`fs_ogle`.`referenceFitsUrl` AS `referenceFitsUrl`,`fs_ogle`.`referenceImageUrl` AS `referenceImageUrl`,`fs_ogle`.`subtractedFitsUrl` AS `subtractedFitsUrl`,`fs_ogle`.`subtractedImageUrl` AS `subtractedImageUrl`,`fs_ogle`.`summaryRow` AS `summaryRow`,`fs_ogle`.`survey` AS `survey`,`fs_ogle`.`surveyObjectUrl` AS `surveyObjectUrl`,`fs_ogle`.`targetFitsUrl` AS `targetFitsUrl`,`fs_ogle`.`targetImageUrl` AS `targetImageUrl`,`fs_ogle`.`transientTypePrediction` AS `transientTypePrediction`,`fs_ogle`.`htm16ID` AS `htm16ID` from `fs_ogle` where `fs_ogle`.`summaryRow` is true */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_object_akas`
--

/*!50001 DROP TABLE IF EXISTS `view_object_akas`*/;
/*!50001 DROP VIEW IF EXISTS `view_object_akas`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_object_akas` AS select `_subview_object_akas`.`transientBucketId` AS `transientBucketId`,`_subview_object_akas`.`primaryKeyId` AS `primaryKeyId`,`_subview_object_akas`.`name` AS `name`,`_subview_object_akas`.`survey` AS `survey`,`_subview_object_akas`.`surveyObjectUrl` AS `surveyObjectUrl`,`_subview_object_akas`.`referenceImageUrl` AS `referenceImageUrl`,`_subview_object_akas`.`targetImageUrl` AS `targetImageUrl`,`_subview_object_akas`.`subtractedImageUrl` AS `subtractedImageUrl`,`_subview_object_akas`.`tripletImageUrl` AS `tripletImageUrl`,`_subview_object_akas`.`finderImageUrl` AS `finderImageUrl` from `_subview_object_akas` group by `_subview_object_akas`.`name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_object_temporal_data`
--

/*!50001 DROP TABLE IF EXISTS `view_object_temporal_data`*/;
/*!50001 DROP VIEW IF EXISTS `view_object_temporal_data`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_object_temporal_data` AS select `transientbucket`.`transientBucketId` AS `transientBucketId`,`transientbucket`.`name` AS `name`,`transientbucket`.`survey` AS `survey`,`transientbucket`.`observationDate` AS `observationDate`,`transientbucket`.`observationMJD` AS `observationMJD`,`transientbucket`.`magnitude` AS `magnitude`,`transientbucket`.`magnitudeError` AS `magnitudeError`,`transientbucket`.`filter` AS `filter`,`transientbucket`.`surveyObjectUrl` AS `surveyObjectUrl`,`transientbucket`.`referenceImageUrl` AS `referenceImageUrl`,`transientbucket`.`targetImageUrl` AS `targetImageUrl`,`transientbucket`.`subtractedImageUrl` AS `subtractedImageUrl`,`transientbucket`.`tripletImageUrl` AS `tripletImageUrl`,`transientbucket`.`telescope` AS `telescope`,`transientbucket`.`instrument` AS `instrument` from `transientbucket` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_objectredshifts`
--

/*!50001 DROP TABLE IF EXISTS `view_objectredshifts`*/;
/*!50001 DROP VIEW IF EXISTS `view_objectredshifts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_objectredshifts` AS select `transientbucket`.`transientBucketId` AS `transientBucketId`,`transientbucket`.`transientRedshift` AS `transientRedshift` from `transientbucket` where `transientbucket`.`transientRedshift` is not null group by `transientbucket`.`transientBucketId` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_objectspectraltypes`
--

/*!50001 DROP TABLE IF EXISTS `view_objectspectraltypes`*/;
/*!50001 DROP VIEW IF EXISTS `view_objectspectraltypes`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_objectspectraltypes` AS select `transientbucket`.`transientBucketId` AS `transientBucketId`,`transientbucket`.`spectralType` AS `spectralType` from `transientbucket` where `transientbucket`.`spectralType` is not null group by `transientbucket`.`transientBucketId` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_tns_photometry_discoveries`
--

/*!50001 DROP TABLE IF EXISTS `view_tns_photometry_discoveries`*/;
/*!50001 DROP VIEW IF EXISTS `view_tns_photometry_discoveries`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_tns_photometry_discoveries` AS select distinct `s`.`raDeg` AS `raDeg`,`s`.`decDeg` AS `decDeg`,`p`.`objectName` AS `objectName`,`p`.`survey` AS `survey`,`p`.`suggestedType` AS `suggestedType`,`s`.`hostRedshift` AS `hostRedshift` from (`tns_sources` `s` join `tns_photometry` `p`) where `s`.`TNSId` = `p`.`TNSId` and `p`.`objectName` is not null */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_transientbucketmaster`
--

/*!50001 DROP TABLE IF EXISTS `view_transientbucketmaster`*/;
/*!50001 DROP VIEW IF EXISTS `view_transientbucketmaster`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_transientbucketmaster` AS select `transientbucket`.`primaryKeyId` AS `primaryKeyId`,`transientbucket`.`transientBucketId` AS `transientBucketId`,`transientbucket`.`masterIDFlag` AS `masterIDFlag`,`transientbucket`.`name` AS `name`,`transientbucket`.`survey` AS `survey`,`transientbucket`.`raDeg` AS `raDeg`,`transientbucket`.`decDeg` AS `decDeg`,`transientbucket`.`raDegErr` AS `raDegErr`,`transientbucket`.`decDegErr` AS `decDegErr`,`transientbucket`.`observationDate` AS `observationDate`,`transientbucket`.`observationMJD` AS `observationMJD`,`transientbucket`.`magnitude` AS `magnitude`,`transientbucket`.`magnitudeError` AS `magnitudeError`,`transientbucket`.`filter` AS `filter`,`transientbucket`.`transientRedshift` AS `transientRedshift`,`transientbucket`.`transientRedshiftNotes` AS `transientRedshiftNotes`,`transientbucket`.`spectralType` AS `spectralType`,`transientbucket`.`discoveryPhase` AS `discoveryPhase`,`transientbucket`.`dateCreated` AS `dateCreated`,`transientbucket`.`dateLastModified` AS `dateLastModified`,`transientbucket`.`surveyObjectUrl` AS `surveyObjectUrl`,`transientbucket`.`transientTypePrediction` AS `transientTypePrediction`,`transientbucket`.`transientTypePredicationSource` AS `transientTypePredicationSource`,`transientbucket`.`hostRedshift` AS `hostRedshift`,`transientbucket`.`hostRedshiftType` AS `hostRedshiftType`,`transientbucket`.`referenceImageUrl` AS `referenceImageUrl`,`transientbucket`.`targetImageUrl` AS `targetImageUrl`,`transientbucket`.`subtractedImageUrl` AS `subtractedImageUrl`,`transientbucket`.`tripletImageUrl` AS `tripletImageUrl`,`transientbucket`.`htm20ID` AS `htm20ID`,`transientbucket`.`htm16ID` AS `htm16ID`,`transientbucket`.`cx` AS `cx`,`transientbucket`.`cy` AS `cy`,`transientbucket`.`cz` AS `cz`,`transientbucket`.`telescope` AS `telescope`,`transientbucket`.`instrument` AS `instrument`,`transientbucket`.`reducer` AS `reducer`,`transientbucket`.`lastNonDetectionDate` AS `lastNonDetectionDate`,`transientbucket`.`lastNonDetectionMJD` AS `lastNonDetectionMJD`,`transientbucket`.`dateLastRead` AS `dateLastRead`,`transientbucket`.`finderImageUrl` AS `finderImageUrl`,`transientbucket`.`lightcurveURL` AS `lightcurveURL` from `transientbucket` where `transientbucket`.`masterIDFlag` = 1 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_wiserep_object_summaries`
--

/*!50001 DROP TABLE IF EXISTS `view_wiserep_object_summaries`*/;
/*!50001 DROP VIEW IF EXISTS `view_wiserep_object_summaries`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013  SQL SECURITY DEFINER */
/*!50001 VIEW `view_wiserep_object_summaries` AS (select `master`.`transientBucketId` AS `transientBucketId`,`master`.`name` AS `name`,`master`.`survey` AS `survey`,`master`.`raDeg` AS `raDeg`,`master`.`decDeg` AS `decDeg`,`spec`.`spectralType` AS `spectralType`,`z`.`transientRedshift` AS `transientRedshift` from ((`transientbucket` `master` left join `view_objectspectraltypes` `spec` on(`spec`.`transientBucketId` = `master`.`transientBucketId` or `spec`.`transientBucketId` is null)) left join `view_objectredshifts` `z` on(`z`.`transientBucketId` = `master`.`transientBucketId` or `z`.`transientBucketId` is null)) where `master`.`masterIDFlag` = 1 and (`z`.`transientRedshift` is not null or `spec`.`spectralType` is not null)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-11 15:08:15
-- MySQL dump 10.17  Distrib 10.3.25-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: 10.131.21.162    Database: marshall
-- ------------------------------------------------------
-- Server version	10.4.17-MariaDB-1:10.4.17+maria~focal-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `meta_workflow_lists_counts`
--

DROP TABLE IF EXISTS `meta_workflow_lists_counts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meta_workflow_lists_counts` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `listname` varchar(100) DEFAULT NULL,
  `count` mediumint(9) DEFAULT NULL,
  PRIMARY KEY (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `primaryId_UNIQUE` (`primaryId`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `listname_unique` (`listname`) KEY_BLOCK_SIZE=1024
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meta_workflow_lists_counts`
--

LOCK TABLES `meta_workflow_lists_counts` WRITE;
/*!40000 ALTER TABLE `meta_workflow_lists_counts` DISABLE KEYS */;
INSERT INTO `meta_workflow_lists_counts` VALUES (1,'archive',117582),(2,'following',43),(3,'followup complete',606),(4,'review for followup',117),(5,'pending observation',25),(6,'inbox',345),(7,'external alert released',7496),(8,'pending classification',8),(9,'pessto classification released',1067),(10,'archived without alert',18678),(11,'queued for atel',0),(17,'classified',14268),(19,'all',118726),(20,'snoozed',29537);
/*!40000 ALTER TABLE `meta_workflow_lists_counts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webapp_users`
--

DROP TABLE IF EXISTS `webapp_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webapp_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) NOT NULL,
  `secondname` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL DEFAULT '$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1',
  `permissions` varchar(45) NOT NULL DEFAULT 'edit_users',
  PRIMARY KEY (`id`) KEY_BLOCK_SIZE=1024,
  UNIQUE KEY `first_second` (`firstname`,`secondname`) KEY_BLOCK_SIZE=1024
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webapp_users`
--

LOCK TABLES `webapp_users` WRITE;
/*!40000 ALTER TABLE `webapp_users` DISABLE KEYS */;
INSERT INTO `webapp_users` VALUES (1,'yen-chen','pan','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(2,'alejandro','clocchiatt','noaccess','edit_users'),(3,'nicolas','jerkstrand','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(4,'anders','nyholm','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(5,'andrea','pastorello','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(6,'andy','howell','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(8,'antonia','morales-garoffolo','noaccess','edit_users'),(9,'ariel','goobar','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(10,'armin','rest','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(11,'Assaf','Sternberg','noaccess','edit_users'),(12,'avet','harutyunyan','noaccess','edit_users'),(13,'avishay','gal-yam','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(14,'brian','schmidt','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(15,'charlie','baltay','noaccess','edit_users'),(16,'chris','ashall','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(17,'christophe','balland','noaccess','edit_users'),(18,'claes','fransson','noaccess','edit_users'),(19,'claudia','gutierrez','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(20,'Cosimo','Inserra','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(21,'cristina','barbarino','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(22,'cristina','knapic','noaccess','edit_users'),(24,'darryl','wright','noaccess','edit_users'),(25,'david','bersier','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(26,'david','rabinowitz','noaccess','edit_users'),(27,'David','Young','$5$rounds=110000$xUZS2oqgUMEL3eSv$.OL5UMZ7lOpDOcZ5LcMZaX.tg/IxZjZeZ/hcapmwcX/','superadmin'),(28,'elisabeth','gall','noaccess','edit_users'),(29,'ellie','hadjiyska','noaccess','edit_users'),(30,'Emille','Ishida','noaccess','edit_users'),(31,'emir','karamehmetoglu','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(32,'emma','riley','noaccess','edit_users'),(33,'emma','walker','noaccess','edit_users'),(34,'enrico','cappellaro','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(35,'eric','hsiao','noaccess','edit_users'),(36,'erkki','kankare','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(37,'fang','yuan','noaccess','edit_users'),(38,'Felipe','Olivares','noaccess','edit_users'),(39,'flora','cellier-holtzem','noaccess','edit_users'),(40,'Francesco','Taddia','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(41,'francisco','forster','noaccess','edit_users'),(42,'franciso','forster','noaccess','edit_users'),(43,'Franz','Bauer','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(44,'Giacomo','Terreran','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(45,'giorgos','dimitriadis','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(46,'Giorgos','Leloudas','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(47,'giuliano','pignata','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(48,'hanindyo','kuncarayakti','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(49,'heather','campbell','noaccess','edit_users'),(50,'Iair','Arcavi','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(51,'isobel','hook','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(52,'jayne','doe','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(53,'jean-baptiste','marquette','noaccess','edit_users'),(54,'jesper','sollerman','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(55,'joe','anderson','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(56,'joe','lyman','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(57,'Joe','Polshaw','noaccess','edit_users'),(58,'joel','johansson','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(59,'john','danziger','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(60,'john','eldridge','noaccess','edit_users'),(61,'jonathan','mackey','noaccess','edit_users'),(62,'jordi','isern','noaccess','edit_users'),(63,'jose','maza','noaccess','edit_users'),(64,'justyn','maund','noaccess','edit_users'),(65,'Katalin','Takats','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(66,'kate','maguire','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(67,'Ken','Smith','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(68,'laura','greggio','noaccess','edit_users'),(69,'laurent','le-guillou','noaccess','edit_users'),(70,'leonardo','tartaglia','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(71,'letizia','pumo','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(72,'linda','astman','noaccess','edit_users'),(73,'lindsay','magill','noaccess','edit_users'),(74,'lluis','galbany','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(75,'luca','zampieri','noaccess','edit_users'),(76,'lukasz','wyrzykowski','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(77,'marco','limongi','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(78,'marco','molinaro','noaccess','edit_users'),(79,'marek','kowalski','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(80,'maria','teresa-botticella','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(81,'mario','hamuy','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(82,'mark','huber','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(83,'Mark','Magee','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(84,'mark','sullivan','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(85,'markus','kromer','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(86,'massimo','dall\'ora','no access','edit_users'),(87,'massimo','della-valle','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(88,'massimo','turatto','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(89,'mathilde','fleury','noaccess','edit_users'),(90,'matt','mccrum','noaccess','edit_users'),(91,'matthew','nicholl','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(92,'mattia','bulla','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(93,'mattias','ergon','noaccess','edit_users'),(94,'max','stritzinger','noaccess','edit_users'),(95,'Michael','Childress','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(96,'michel','dennefeld','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(97,'milena','bufano','noaccess','edit_users'),(98,'morgan','fraser','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(99,'nadejda','blagorodnova','noaccess','edit_users'),(100,'nancy','elias-rosa','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(101,'nando','patat','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(102,'neil','meharg','noaccess','edit_users'),(103,'nicholas','walton','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(104,'nicolas','regnault','noaccess','edit_users'),(105,'norbert','langer','noaccess','edit_users'),(106,'ofer','yaron','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(107,'Paolo','Mazzali','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(108,'peter','lundqvist','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(109,'peter','nugent','noaccess','edit_users'),(110,'phil','james','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(111,'Philipp','Podsiadlowski','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(112,'pierre-francois','leget','noaccess','edit_users'),(113,'pignata','giuliano','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(114,'rahman','amanullah','noaccess','edit_users'),(115,'reynald','pain','noaccess','edit_users'),(116,'ricardo','smareglia','noaccess','edit_users'),(117,'richard','scalzo','noaccess','edit_users'),(118,'robert','firth','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(119,'rubina','kotak','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(120,'sandra','benitez','noaccess','edit_users'),(121,'santiago','gonzalez','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(122,'sebastien','bongard','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(123,'seppo','mattila','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(124,'simon','hodgkin','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(125,'sina','rostami','noaccess','edit_users'),(126,'stefan','taubenberger','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(127,'stefano','benetti','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(128,'Stefano','Valenti','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(129,'stephan','hachinger','noaccess','edit_users'),(130,'stephane','blondin','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(131,'Stephen','Smartt','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(132,'steve','schulze','$5$rounds=535000$lvgXQqIE4vM639YE$1kjpM2QxUBJ4KGRpqtOIrONeplIJ0KhNetB1.I9tdbA','edit_users'),(133,'steven','margheim','noaccess','edit_users'),(134,'stuart','sim','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(135,'susanna','spiro','noaccess','edit_users'),(136,'sylvain','baumont','noaccess','edit_users'),(137,'Thomas','De','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(138,'Ting-Wan','Chen','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(139,'tuomas','kangas','noaccess','edit_users'),(140,'ulrich','feindt','noaccess','edit_users'),(141,'Vahagn','Harutyunyan','noaccess','edit_users'),(142,'vallery','stanishev','noaccess','edit_users'),(143,'wolfgang','hillebrandt','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(145,'griffin','hosseinzadeh','noaccess','edit_users'),(147,'nicolas','chotard','noaccess','edit_users'),(149,'fang','huang','noaccess','edit_users'),(151,'marine','ducrot','noaccess','edit_users'),(153,'matt','smith','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(155,'jussi','harmanen','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(157,'christoffer','fremling','noaccess','edit_users'),(159,'john','doe','noaccess','edit_users'),(161,'mikael','normann','noaccess','edit_users'),(163,'katia','migotto','noaccess','edit_users'),(165,'lina','tomasella','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(167,'paula','zelaya','noaccess','edit_users'),(169,'sergio','campana','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(171,'chris','frohmaier','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(173,'natasha','karpenka','noaccess','edit_users'),(175,'regis','cartier','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(177,'szymon','prajs','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(179,'ken','chambers','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(181,'steven','williams','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(183,'assaf','horesh','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(185,'heather','flewelling','noaccess','edit_users'),(186,'alessandro','razza','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(187,'ismael','pessa','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(188,'tania','moraga','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(189,'claudia','agliozzo','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(190,'patrice','bouchet','noaccess','edit_users'),(191,'simon','prentice','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(192,'thomas','de.jaeger','noaccess','edit_users'),(193,'kate','furnell','noaccess','edit_users'),(194,'john','tonry','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(195,'larry','denneau','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(196,'andrei','sherst','noaccess','edit_users'),(197,'brian','stalder','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(198,'aren','heinze','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(200,'michele','sasdelli','noaccess','edit_users'),(201,'remy.le','breton','noaccess','edit_users'),(202,'ilan','manulis','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(203,'ayan','mitra','noaccess','edit_users'),(204,'aleksandar','cikota','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(205,'tamar','faran','noaccess','edit_users'),(206,'peter','jonker','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(207,'nancy','ellman','noaccess','edit_users'),(208,'curtis','mccully','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(209,'ira','bar','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(211,'anais','moller','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(212,'brad','tucker','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(213,'tom','reynolds','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(214,'ashley','ruiter','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(215,'ivo','seitenzahl','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(216,'bonnie','zhang','noaccess','edit_users'),(217,'lawrence','short','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(218,'michael','coughlin','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(219,'peter','clark','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(220,'miika','pursiainen','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(221,'pilar','ruiz-lapuente','noaccess','edit_users'),(222,'azalee','bostroem','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(223,'lixin','yu','noaccess','edit_users'),(224,'lingzhi','wang','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(225,'osmar','rodriguez','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(226,'david','oneill','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(227,'yongzhi','cai','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(228,'andreas','floers','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(229,'zach','cano','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(230,'silvia','piranomonte','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(231,'francesca','onori','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(232,'aleksandra','hamanowicz','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(233,'rupak','roy','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(234,'paolo','davanzo','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(235,'eliana','palazzi','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(236,'giacomo','cannizzaro','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(237,'mariusz','gromadzki','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(238,'jan','bolmer','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(239,'stefano','covino','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(240,'frederic','daigne','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(241,'valerio','d.elia','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(242,'kasper.elm','heintz','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(243,'andrea','melandri','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(244,'jesse','palmerio','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(245,'andrea','rossi','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(246,'boris','sbarufatti','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(247,'pat','schady','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(248,'giulia','stratta','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(249,'gianpiero','tagliaferri','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(250,'susanna','vergani','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(251,'luca','izzo','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(252,'krzysztof','rybicki','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(253,'daniel','kusters','noaccess','edit_users'),(254,'marica','branchesi','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(258,'nicola','masetti','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(259,'jakob','nordin','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(260,'anna','franckowiak','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(262,'mickael','rigault','noaccess','edit_users'),(264,'nora','strotjohann','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(265,'valery','brinnel','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(266,'jakob','van.santen','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(267,'matteo','giomi','noaccess','edit_users'),(270,'paul','groot','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(271,'enzo','brocato','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(272,'zuzanna','kostrzewa','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(273,'luke','shingles','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(274,'maria','patterson','$5$rounds=535000$HFlOOKhWYrcCGuB9$qPERc0JMQ8Rp4GOECwBxMHR7BLua1jqVRXgR4YJlUV6','view_users'),(275,'tim','naylor','$5$rounds=535000$HFlOOKhWYrcCGuB9$qPERc0JMQ8Rp4GOECwBxMHR7BLua1jqVRXgR4YJlUV6','view_users'),(276,'carlos','contreras','$5$rounds=535000$HFlOOKhWYrcCGuB9$qPERc0JMQ8Rp4GOECwBxMHR7BLua1jqVRXgR4YJlUV6','view_users'),(277,'roberta','carini','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(278,'david','homan','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(279,'christian','vogl','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(280,'zhitong','li','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(281,'annalisa','de.cia','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(282,'filomena','bufano','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(283,'marco','berton','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(284,'elena','mason','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(285,'paolo','ochner','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(286,'andy','lawrence','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(287,'charlotte','angus','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(288,'luc','dessart','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(289,'daniel','perley','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(292,'zhihao','chen','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(293,'nikola','knezevic','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(294,'owen','mcbrien','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(295,'dave','morris','$5$rounds=535000$HFlOOKhWYrcCGuB9$qPERc0JMQ8Rp4GOECwBxMHR7BLua1jqVRXgR4YJlUV6','view_users'),(296,'emma','callis','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(297,'phil','wiseman','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(298,'roy','williams','$5$rounds=535000$HFlOOKhWYrcCGuB9$qPERc0JMQ8Rp4GOECwBxMHR7BLua1jqVRXgR4YJlUV6','view_users'),(299,'daniele','malesani','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(300,'lana','salmon','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(301,'antonio','martin.carrillo','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(302,'lorraine','hanlon','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(303,'david','murphy','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(304,'david','sand','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(305,'ruoyu','zhu','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(306,'achille','fiore','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(307,'kristhell','lopez','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(312,'christa','gall','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(313,'wolfgang','kerzendorf','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(314,'shane','moran','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(315,'sadie','jones','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(316,'thomas','wevers','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(317,'john','lightfoot','$5$rounds=535000$HFlOOKhWYrcCGuB9$qPERc0JMQ8Rp4GOECwBxMHR7BLua1jqVRXgR4YJlUV6','view_users'),(318,'enrico','congiu','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(319,'adam','rubin','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(320,'massimiliano','de.pasquale','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(321,'priscila','pessi','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(322,'maayane.tamar','soumag','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(323,'daichi','hiramatsu','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(324,'jamie','burke','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(325,'tomas','muller','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(326,'robert','stein','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(327,'noel','castro.segura','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(328,'matthew','grayling','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(329,'philip','short','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(330,'tassilo','schweyer','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(331,'matt','nicholl','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(332,'jen','hjorth','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(333,'ilya','mandel','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(334,'felipe','olivares.estay','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(335,'jonathan','pineda','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(336,'andrea','reguitti','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(337,'jens','hjorth','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(338,'ana','sagues.carracedo','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(339,'sasha','kozyreva','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(340,'fabio','ragosta','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(341,'kelly','skillen','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(344,'deepak','eappachen','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(350,'maria','vincenzi','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(351,'craig','pellegrino','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(352,'lisa','kelsey','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(353,'sean','brennan','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(354,'barnabas','barna','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(355,'jacob','teffs','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(361,'nada','ihanec','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(362,'ignacio','sanchez','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(363,'elizabeth','swann','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(365,'ido','irani','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(366,'teppo','heikkila','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(367,'marco','landoni','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','52'),(368,'shubham','srivastav','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(369,'nico','meza','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(370,'laureano','martinez','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(371,'takashi','nagao','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(372,'jose','prieto','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(373,'juanita','antilen','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(374,'yize','dong','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(375,'michael','lundquist','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(376,'jennifer','andrews','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(377,'sam','wyatt','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(378,'rachael','amaro','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(379,'emmanouela','paraskeva','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(380,'kuntal','mistra','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(382,'samantha','goldwasser','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(383,'miguel','perez-torres','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(384,'matthew','temple','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(387,'meg','schwamb','$5$rounds=535000$HFlOOKhWYrcCGuB9$qPERc0JMQ8Rp4GOECwBxMHR7BLua1jqVRXgR4YJlUV6','view_users'),(388,'rachel','bruch','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(391,'james','gillanders','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(394,'panos','charalampopoulos','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(395,'eleonora','parrag','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(396,'michael','fulton','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(397,'giorgio','valerin','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(398,'pietro','schipani','$5$rounds=535000$HFlOOKhWYrcCGuB9$qPERc0JMQ8Rp4GOECwBxMHR7BLua1jqVRXgR4YJlUV6','view_users'),(399,'kyle','medler','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(400,'cristina','cristina','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(401,'emma','reilly','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(402,'nicolas','meza','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(403,'erez','zimmerman','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(404,'melissa','amenouche','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(406,'maxime','deckers','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(407,'arianna','zanon','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(409,'antonia','morales.garoffolo','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(410,'kuntal','misra','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(411,'anne','inkenhaag','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(412,'quinn','wang','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(413,'ryan','ridden.harper','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(414,'este','padilla.gonzalez','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(415,'admin','user','$5$rounds=535000$tOu/3ZMR75.Iujrt$jj07weVdX0TPe933hE0dEeW7wTOFJfl4R1u1yqz6tu.','superadmin'),(416,'scott','davis','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(417,'zheng','cao','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(418,'evan','ridley','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(419,'lydia','makrygianni','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(420,'sheng','yang','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(421,'robert','byrne','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(422,'ragnhild','lunnan','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(425,'maria','delgado','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(428,'raul','gonzalez','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users'),(431,'sara','munoz','$5$rounds=110000$MAKWStjFVWb2dqhG$oqBc8072dGM.mtWRmEFQ.WnhSZ79hn9yphtE8QflxT1','edit_users');
/*!40000 ALTER TABLE `webapp_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_ssdr1_overview`
--

DROP TABLE IF EXISTS `stats_ssdr1_overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_ssdr1_overview` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `filetype` varchar(200) DEFAULT NULL,
  `numberOfFiles` int(11) DEFAULT NULL,
  `dataVolumeBytes` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_ssdr1_overview`
--

LOCK TABLES `stats_ssdr1_overview` WRITE;
/*!40000 ALTER TABLE `stats_ssdr1_overview` DISABLE KEYS */;
INSERT INTO `stats_ssdr1_overview` VALUES (1,'sofi_science_images',234,1946643840),(2,'sofi_image_weights',234,1946612160),(3,'sofi_2d_spectral_images',95,312212160),(4,'sofi_1d_binary_spectra',95,4377600),(5,'efosc_acq_images',977,4020863040),(6,'efosc_science_images',1996,7731239040),(7,'efosc_2d_spectral_images',813,2793409920),(27,'efosc_1d_binary_spectra',813,37463040);
/*!40000 ALTER TABLE `stats_ssdr1_overview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_ssdr2_overview`
--

DROP TABLE IF EXISTS `stats_ssdr2_overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_ssdr2_overview` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `filetype` varchar(200) DEFAULT NULL,
  `numberOfFiles` int(11) DEFAULT NULL,
  `dataVolumeBytes` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_ssdr2_overview`
--

LOCK TABLES `stats_ssdr2_overview` WRITE;
/*!40000 ALTER TABLE `stats_ssdr2_overview` DISABLE KEYS */;
INSERT INTO `stats_ssdr2_overview` VALUES (1,'sofi_science_images',158,1265532480),(2,'sofi_image_weights',158,1265480640),(3,'sofi_2d_spectral_images',22,72869760),(4,'sofi_1d_binary_spectra',22,1013760),(5,'efosc_acq_images',1431,5889309120),(6,'efosc_science_images',3504,11551662720),(7,'efosc_2d_spectral_images',798,2735251200),(8,'efosc_1d_binary_spectra',798,36757440);
/*!40000 ALTER TABLE `stats_ssdr2_overview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_ssdr3_overview`
--

DROP TABLE IF EXISTS `stats_ssdr3_overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_ssdr3_overview` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `filetype` varchar(200) DEFAULT NULL,
  `numberOfFiles` int(11) DEFAULT NULL,
  `dataVolumeBytes` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`primaryId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_ssdr3_overview`
--

LOCK TABLES `stats_ssdr3_overview` WRITE;
/*!40000 ALTER TABLE `stats_ssdr3_overview` DISABLE KEYS */;
INSERT INTO `stats_ssdr3_overview` VALUES (1,'sofi_science_images',383,2931883200),(2,'sofi_image_weights',383,2931730560),(3,'sofi_2d_spectral_images',108,355032000),(4,'sofi_1d_binary_spectra',108,4976640),(5,'efosc_acq_images',0,0),(6,'efosc_science_images',7279,25519296960),(7,'efosc_2d_spectral_images',1240,4259767680),(8,'efosc_1d_binary_spectra',1240,57139200);
/*!40000 ALTER TABLE `stats_ssdr3_overview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marshall_fs_column_map`
--

DROP TABLE IF EXISTS `marshall_fs_column_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marshall_fs_column_map` (
  `primaryId` int(11) NOT NULL AUTO_INCREMENT,
  `fs_table_name` varchar(45) NOT NULL,
  `fs_survey_name` varchar(45) DEFAULT NULL,
  `transientBucket_column` varchar(45) DEFAULT NULL,
  `fs_table_column` varchar(45) NOT NULL,
  PRIMARY KEY (`primaryId`),
  UNIQUE KEY `unquie_fs_table_name_fs_table_column` (`fs_table_name`,`fs_table_column`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marshall_fs_column_map`
--

LOCK TABLES `marshall_fs_column_map` WRITE;
/*!40000 ALTER TABLE `marshall_fs_column_map` DISABLE KEYS */;
INSERT INTO `marshall_fs_column_map` VALUES (18,'fs_asassn_sne','ASAS-SN','observationDate','Date'),(21,'fs_asassn_sne','ASAS-SN','name','ID'),(24,'fs_asassn_sne','ASAS-SN','raDeg','RA'),(28,'fs_asassn_sne','ASAS-SN','magnitude','V_disc'),(29,'fs_asassn_sne','ASAS-SN','decDeg','decl'),(30,'fs_asassn_sne','ASAS-SN','surveyObjectUrl','surveyUrl'),(32,'fs_asassn_transients','ASAS-SN','magnitude','Vmag'),(34,'fs_asassn_transients','ASAS-SN','decDeg','decDeg'),(35,'fs_asassn_transients','ASAS-SN','observationDate','discDate'),(36,'fs_asassn_transients','ASAS-SN','name','name'),(37,'fs_asassn_transients','ASAS-SN','raDeg','raDeg'),(38,'fs_asassn_transients','ASAS-SN','spectralType','specClass'),(40,'fs_asassn_transients','ASAS-SN','surveyObjectUrl','surveyUrl'),(47,'fs_atlas','ATLAS','name','candidateID'),(48,'fs_atlas','ATLAS','raDeg','ra_deg'),(49,'fs_atlas','ATLAS','decDeg','dec_deg'),(50,'fs_atlas','ATLAS','magnitude','mag'),(51,'fs_atlas','ATLAS','magnitudeError','magErr'),(52,'fs_atlas','ATLAS','filter','filter'),(53,'fs_atlas','ATLAS','observationMJD','observationMJD'),(54,'fs_atlas','ATLAS','observationDate','discDate'),(56,'fs_atlas','ATLAS','transientTypePrediction','suggestedType'),(58,'fs_atlas','ATLAS','hostRedshift','hostZ'),(59,'fs_atlas','ATLAS','targetImageUrl','targetImageURL'),(60,'fs_atlas','ATLAS','referenceImageUrl','refImageURL'),(61,'fs_atlas','ATLAS','subtractedImageUrl','diffImageURL'),(62,'fs_atlas','ATLAS','surveyObjectUrl','objectURL'),(79,'fs_atlas_forced_phot','ATLAS FP','name','atlas_designation'),(80,'fs_atlas_forced_phot','ATLAS FP','observationMJD','mjd_obs'),(81,'fs_atlas_forced_phot','ATLAS FP','filter','filter'),(87,'fs_atlas_forced_phot','ATLAS FP','raDeg','raDeg'),(88,'fs_atlas_forced_phot','ATLAS FP','decDeg','decDeg'),(107,'fs_atlas_forced_phot','ATLAS FP','magnitude','marshall_mag'),(108,'fs_atlas_forced_phot','ATLAS FP','limitingMag','marshall_limiting_mag'),(109,'fs_atlas_forced_phot','ATLAS','magnitudeError','marshall_mag_error'),(191,'fs_crts_css','CRTS','decDeg','decDeg'),(192,'fs_crts_css','CRTS','filter','filter'),(193,'fs_crts_css','CRTS','finderImageUrl','finderChartUrl'),(196,'fs_crts_css','CRTS','lightcurveURL','lightcurveUrl'),(197,'fs_crts_css','CRTS','magnitude','mag'),(198,'fs_crts_css','CRTS','name','name'),(199,'fs_crts_css','CRTS','observationDate','observationDate'),(200,'fs_crts_css','CRTS','observationMJD','observationMJD'),(201,'fs_crts_css','CRTS','raDeg','raDeg'),(202,'fs_crts_css','CRTS','surveyObjectUrl','surveyObjectUrl'),(203,'fs_crts_css','CRTS','targetImageUrl','targetImageUrl'),(204,'fs_crts_css','CRTS','transientTypePrediction','transientTypePrediction'),(206,'fs_crts_css','CRTS','magnitudeError','magErr'),(207,'fs_crts_css','CRTS','lastNonDetectionDate','lastNonDetectionDate'),(208,'fs_crts_css','CRTS','lastNonDetectionMJD','lastNonDetectionMJD'),(222,'fs_crts_mls','CRTS','decDeg','decDeg'),(223,'fs_crts_mls','CRTS','filter','filter'),(224,'fs_crts_mls','CRTS','finderImageUrl','finderChartUrl'),(227,'fs_crts_mls','CRTS','lightcurveURL','lightcurveUrl'),(228,'fs_crts_mls','CRTS','magnitude','mag'),(229,'fs_crts_mls','CRTS','name','name'),(230,'fs_crts_mls','CRTS','observationDate','observationDate'),(231,'fs_crts_mls','CRTS','observationMJD','observationMJD'),(232,'fs_crts_mls','CRTS','raDeg','raDeg'),(233,'fs_crts_mls','CRTS','surveyObjectUrl','surveyObjectUrl'),(234,'fs_crts_mls','CRTS','targetImageUrl','targetImageUrl'),(235,'fs_crts_mls','CRTS','transientTypePrediction','transientTypePrediction'),(237,'fs_crts_mls','CRTS','magnitudeError','magErr'),(238,'fs_crts_mls','CRTS','lastNonDetectionDate','lastNonDetectionDate'),(239,'fs_crts_mls','CRTS','lastNonDetectionMJD','lastNonDetectionMJD'),(253,'fs_crts_sss','CRTS','decDeg','decDeg'),(254,'fs_crts_sss','CRTS','filter','filter'),(255,'fs_crts_sss','CRTS','finderImageUrl','finderChartUrl'),(258,'fs_crts_sss','CRTS','lightcurveURL','lightcurveUrl'),(259,'fs_crts_sss','CRTS','magnitude','mag'),(260,'fs_crts_sss','CRTS','name','name'),(261,'fs_crts_sss','CRTS','observationDate','observationDate'),(262,'fs_crts_sss','CRTS','observationMJD','observationMJD'),(263,'fs_crts_sss','CRTS','raDeg','raDeg'),(264,'fs_crts_sss','CRTS','surveyObjectUrl','surveyObjectUrl'),(265,'fs_crts_sss','CRTS','targetImageUrl','targetImageUrl'),(266,'fs_crts_sss','CRTS','transientTypePrediction','transientTypePrediction'),(268,'fs_crts_sss','CRTS','magnitudeError','magErr'),(269,'fs_crts_sss','CRTS','lastNonDetectionDate','lastNonDetectionDate'),(270,'fs_crts_sss','CRTS','lastNonDetectionMJD','lastNonDetectionMJD'),(280,'fs_des','DES','decDeg','decDeg'),(281,'fs_des','DES','filter','filter'),(282,'fs_des','DES','lastNonDetectionDate','lastNonDetectionDate'),(283,'fs_des','DES','lastNonDetectionMJD','lastNonDetectionMJD'),(284,'fs_des','DES','limitingMag','limitingMag'),(285,'fs_des','DES','magnitude','magnitude'),(286,'fs_des','DES','magnitudeError','magnitudeError'),(287,'fs_des','DES','name','name'),(288,'fs_des','DES','observationDate','observationDate'),(289,'fs_des','DES','observationMJD','observationMJD'),(290,'fs_des','DES','raDeg','raDeg'),(293,'fs_des','DES','surveyObjectUrl','surveyUrl'),(294,'fs_des','DES','transientTypePrediction','transientTypePrediction'),(295,'fs_des','DES','finderImageUrl','finderImageUrl'),(296,'fs_des','DES','subtractedImageUrl','diffUrl'),(297,'fs_des','DES','referenceImageUrl','refUrl'),(298,'fs_des','DES','targetImageUrl','tarUrl'),(311,'fs_gaia','Gaia','name','candidateID'),(312,'fs_gaia','Gaia','decDeg','dec_deg'),(313,'fs_gaia','Gaia','observationDate','discDate'),(315,'fs_gaia','Gaia','filter','filter'),(316,'fs_gaia','Gaia','magnitude','mag'),(317,'fs_gaia','Gaia','surveyObjectUrl','objectURL'),(318,'fs_gaia','Gaia','observationMJD','observationMJD'),(319,'fs_gaia','Gaia','raDeg','ra_deg'),(389,'fs_master','MASTER','tripletImageUrl','imageUrl'),(390,'fs_master','MASTER','magnitude','magnitude'),(392,'fs_master','MASTER','name','name'),(394,'fs_master','MASTER','transientTypePrediction','type'),(395,'fs_master','MASTER','observationMJD','discoveryMjd'),(396,'fs_master','MASTER','decDeg','decDeg'),(397,'fs_master','MASTER','raDeg','raDeg'),(398,'fs_master','MASTER','filter','filter'),(399,'fs_master','MASTER','surveyObjectUrl','candidateUrl'),(420,'fs_ogle','OGLE','decDeg','decDeg'),(421,'fs_ogle','OGLE','filter','filter'),(422,'fs_ogle','OGLE','lastNonDetectionDate','lastNonDetectionDate'),(423,'fs_ogle','OGLE','lastNonDetectionMJD','lastNonDetectionMJD'),(424,'fs_ogle','OGLE','lightcurveURL','lightcurveUrl'),(425,'fs_ogle','OGLE','magnitude','mag'),(426,'fs_ogle','OGLE','name','name'),(427,'fs_ogle','OGLE','observationDate','observationDate'),(428,'fs_ogle','OGLE','observationMJD','observationMJD'),(429,'fs_ogle','OGLE','raDeg','raDeg'),(431,'fs_ogle','OGLE','referenceImageUrl','referenceImageUrl'),(433,'fs_ogle','OGLE','subtractedImageUrl','subtractedImageUrl'),(434,'fs_ogle','OGLE','surveyObjectUrl','surveyObjectUrl'),(436,'fs_ogle','OGLE','targetImageUrl','targetImageUrl'),(437,'fs_ogle','OGLE','transientTypePrediction','transientTypePrediction'),(440,'fs_ogle','OGLE','magnitudeError','magErr'),(441,'fs_ogle','OGLE','limitingMag','limitingMag'),(450,'fs_panstarrs','PanSTARRS','name','candidateID'),(451,'fs_panstarrs','PanSTARRS','raDeg','ra_deg'),(452,'fs_panstarrs','PanSTARRS','decDeg','dec_deg'),(453,'fs_panstarrs','PanSTARRS','magnitude','mag'),(454,'fs_panstarrs','PanSTARRS','magnitudeError','magErr'),(455,'fs_panstarrs','PanSTARRS','filter','filter'),(456,'fs_panstarrs','PanSTARRS','observationMJD','observationMJD'),(457,'fs_panstarrs','PanSTARRS','observationDate','discDate'),(459,'fs_panstarrs','PanSTARRS','transientTypePrediction','suggestedType'),(461,'fs_panstarrs','PanSTARRS','hostRedshift','hostZ'),(462,'fs_panstarrs','PanSTARRS','targetImageUrl','targetImageURL'),(463,'fs_panstarrs','PanSTARRS','referenceImageUrl','refImageURL'),(464,'fs_panstarrs','PanSTARRS','subtractedImageUrl','diffImageURL'),(465,'fs_panstarrs','PanSTARRS','surveyObjectUrl','objectURL'),(481,'fs_skymapper','SkyMapper','decDeg','DECL'),(482,'fs_skymapper','SkyMapper','raDeg','RA'),(483,'fs_skymapper','SkyMapper','transientTypePrediction','bestType'),(484,'fs_skymapper','SkyMapper','name','candidateID'),(485,'fs_skymapper','SkyMapper','surveyObjectUrl','candidateURL'),(488,'fs_skymapper','SkyMapper','subtractedImageUrl','diffThumbURL'),(492,'fs_skymapper','SkyMapper','filter','filt'),(493,'fs_skymapper','SkyMapper','magnitude','mag'),(494,'fs_skymapper','SkyMapper','magnitudeError','magerr'),(495,'fs_skymapper','SkyMapper','observationMJD','mjd'),(496,'fs_skymapper','SkyMapper','targetImageUrl','newThumbURL'),(498,'fs_skymapper','SkyMapper','lastNonDetectionMJD','noneMJD'),(501,'fs_skymapper','SkyMapper','referenceImageUrl','refThumbURL'),(512,'fs_tns_transients',NULL,'decDeg','decDeg'),(514,'fs_tns_transients',NULL,'observationDate','discDate'),(515,'fs_tns_transients',NULL,'magnitude','discMag'),(516,'fs_tns_transients',NULL,'filter','discMagFilter'),(519,'fs_tns_transients',NULL,'hostRedshift','hostRedshift'),(520,'fs_tns_transients',NULL,'name','objectName'),(521,'fs_tns_transients',NULL,'surveyObjectUrl','objectUrl'),(522,'fs_tns_transients',NULL,'raDeg','raDeg'),(525,'fs_tns_transients',NULL,'spectralType','specType'),(526,'fs_tns_transients',NULL,'transientRedshift','transRedshift'),(527,'fs_tns_transients',NULL,'lastNonDetectionDate','lastNonDetectionDate'),(530,'fs_tns_transients',NULL,'lastNonDetectionDate','lastNonDetectionDateParsed'),(558,'fs_user_added',NULL,'name','candidateID'),(559,'fs_user_added',NULL,'raDeg','ra_deg'),(560,'fs_user_added',NULL,'decDeg','dec_deg'),(561,'fs_user_added',NULL,'magnitude','mag'),(562,'fs_user_added',NULL,'magnitudeError','magErr'),(563,'fs_user_added',NULL,'filter','filter'),(564,'fs_user_added',NULL,'observationMJD','observationMJD'),(565,'fs_user_added',NULL,'observationDate','discDate'),(567,'fs_user_added',NULL,'transientTypePrediction','suggestedType'),(569,'fs_user_added',NULL,'hostRedshift','hostZ'),(570,'fs_user_added',NULL,'targetImageUrl','targetImageURL'),(571,'fs_user_added',NULL,'surveyObjectUrl','objectURL'),(589,'fs_ztf','ZTF','name','objectId'),(590,'fs_ztf','ZTF','raDeg','raDeg'),(591,'fs_ztf','ZTF','decDeg','decDeg'),(592,'fs_ztf','ZTF','observationMJD','mjd'),(594,'fs_ztf','ZTF','magnitude','magpsf'),(595,'fs_ztf','ZTF','magnitudeError','sigmapsf'),(600,'fs_ztf','ZTF','filter','filt'),(601,'fs_ztf','ZTF','surveyObjectUrl','surveyUrl'),(602,'fs_ztf','ZTF','tripletImageUrl','tripletImageUrl'),(604,'fs_ztf','ZTF','limitingMag','limitingMag'),(793,'atel_coordinates',NULL,'raDeg','raDeg'),(794,'atel_coordinates',NULL,'decDeg','decDeg'),(798,'atel_coordinates',NULL,'name','atelName'),(799,'atel_coordinates',NULL,'surveyObjectUrl','atelUrl'),(1017,'fs_tns_transients',NULL,'survey','survey'),(1018,'fs_user_added',NULL,'survey','survey'),(1021,'tns_sources','TNS','name','TNSName'),(1022,'tns_sources','TNS','decDeg','decDeg'),(1024,'tns_sources','TNS','observationDate','discDate'),(1025,'tns_sources','TNS','magnitude','discMag'),(1026,'tns_sources','TNS','filter','discMagFilter'),(1029,'tns_sources','TNS','surveyObjectUrl','objectUrl'),(1030,'tns_sources','TNS','raDeg','raDeg'),(1031,'tns_sources','TNS','spectralType','specType'),(1033,'tns_sources','TNS','transientRedshift','transRedshift'),(1035,'tns_sources','TNS','hostRedshift','hostRedshift'),(1040,'tns_spectra',NULL,'observationDate','obsdate'),(1042,'tns_spectra',NULL,'spectralType','specType'),(1044,'tns_spectra',NULL,'transientRedshift','transRedshift'),(1047,'tns_spectra',NULL,'observationMJD','observationMJD'),(1053,'tns_spectra',NULL,'name','TNSName'),(1055,'tns_spectra',NULL,'raDeg','raDeg'),(1056,'tns_spectra',NULL,'decDeg','decDeg'),(1060,'tns_photometry',NULL,'filter','filter'),(1061,'tns_photometry',NULL,'limitingMag','limitingMag'),(1062,'tns_photometry',NULL,'magnitude','mag'),(1063,'tns_photometry',NULL,'magnitudeError','magErr'),(1065,'tns_photometry',NULL,'name','objectName'),(1066,'tns_photometry',NULL,'observationDate','obsdate'),(1069,'tns_photometry',NULL,'survey','survey'),(1072,'tns_photometry',NULL,'observationMJD','observationMJD'),(1088,'tns_spectra',NULL,'survey','survey'),(1089,'tns_photometry',NULL,'raDeg','raDeg'),(1090,'tns_photometry',NULL,'decDeg','decDeg');
/*!40000 ALTER TABLE `marshall_fs_column_map` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-11 15:08:15
