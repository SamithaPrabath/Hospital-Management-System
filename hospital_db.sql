-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: hospital_db
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `doctor_id` int NOT NULL,
  `staff_id` int NOT NULL,
  `specialization_id` int DEFAULT NULL,
  `status` varchar(45) DEFAULT 'Not Available',
  `price` float DEFAULT NULL,
  PRIMARY KEY (`doctor_id`,`staff_id`),
  KEY `fk_doctor_specilization_idx` (`specialization_id`),
  CONSTRAINT `fk_doctor_specilization` FOREIGN KEY (`specialization_id`) REFERENCES `doctor_specialization` (`specialization_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_staff_id_doctor` FOREIGN KEY (`doctor_id`) REFERENCES `staff` (`staff_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1002,1002,1,'Available',3000),(1003,1003,1,'Available',5000);
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_specialization`
--

DROP TABLE IF EXISTS `doctor_specialization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_specialization` (
  `specialization_id` int NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`specialization_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_specialization`
--

LOCK TABLES `doctor_specialization` WRITE;
/*!40000 ALTER TABLE `doctor_specialization` DISABLE KEYS */;
INSERT INTO `doctor_specialization` VALUES (1,'Cardiologist','specialist in heart'),(2,'Neurologist','specialist in nervous system and brain'),(3,'Orthopedic surgeon','specialist in bone structure'),(4,'Oncologist','specialist in cancers'),(5,'Gastroenterologist',' specialist in digestive system'),(6,'Urologist','specialist in urinary tract');
/*!40000 ALTER TABLE `doctor_specialization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medical_report`
--

DROP TABLE IF EXISTS `medical_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_report` (
  `report_id` int DEFAULT NULL,
  `receipt_id` int DEFAULT NULL,
  `image` text,
  `description` text,
  `issued_by` int DEFAULT NULL,
  `issued_date` datetime DEFAULT NULL,
  KEY `fk_recipet_id_idx` (`receipt_id`),
  KEY `fk_staff_id_idx` (`issued_by`),
  CONSTRAINT `fk_recipet_medical_report` FOREIGN KEY (`receipt_id`) REFERENCES `receipt` (`receipt_id`),
  CONSTRAINT `fk_staff_medical_report` FOREIGN KEY (`issued_by`) REFERENCES `staff` (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_report`
--

LOCK TABLES `medical_report` WRITE;
/*!40000 ALTER TABLE `medical_report` DISABLE KEYS */;
INSERT INTO `medical_report` VALUES (1,99481663,'Screenshot_from_2024-12-24_20-41-27.png','bfhjsdbfshdbf',1003,'2024-12-26 18:34:55'),(2,99481663,'Screenshot_from_2024-12-24_16-12-48.png','dsvdfdf',1003,'2024-12-26 18:35:13'),(1,65467108,'Screenshot_from_2024-12-24_16-12-48.png','Test',1003,'2024-12-27 13:29:26');
/*!40000 ALTER TABLE `medical_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `nic` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `address` text,
  `registerd_by` int DEFAULT NULL,
  `registerd_date` datetime DEFAULT NULL,
  PRIMARY KEY (`patient_id`,`nic`),
  KEY `fk_registered_by_idx` (`registerd_by`),
  CONSTRAINT `fk_registered_by` FOREIGN KEY (`registerd_by`) REFERENCES `staff` (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (101,'199900511332','Samitha',25,'468/5b Piliyandala Road, Godigamuwa, Maharagama',1001,'2024-12-22 00:00:00');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_phone`
--

DROP TABLE IF EXISTS `patient_phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_phone` (
  `patient_id` int NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  PRIMARY KEY (`patient_id`,`phone_number`),
  CONSTRAINT `fk_patient_phone` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_phone`
--

LOCK TABLES `patient_phone` WRITE;
/*!40000 ALTER TABLE `patient_phone` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `payment_id` int NOT NULL,
  `receipt_id` int DEFAULT NULL,
  `collected_by` int DEFAULT NULL,
  `collected_date` datetime DEFAULT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `fk_receipt_id_idx` (`receipt_id`),
  KEY `fk_staff_id_idx` (`collected_by`),
  CONSTRAINT `fk_receipt_payment` FOREIGN KEY (`receipt_id`) REFERENCES `receipt` (`receipt_id`),
  CONSTRAINT `fk_staff_payment` FOREIGN KEY (`collected_by`) REFERENCES `staff` (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (31577642,99481663,1002,'2024-12-22 23:50:53'),(42974732,99481663,1002,'2024-12-22 23:57:33');
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt`
--

DROP TABLE IF EXISTS `receipt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt` (
  `receipt_id` int NOT NULL,
  `patient_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `issued_by` int DEFAULT NULL,
  `issued_date` datetime DEFAULT NULL,
  `total_amount` float DEFAULT NULL,
  `status_id` int DEFAULT '0',
  PRIMARY KEY (`receipt_id`),
  KEY `fk_patient_id_idx` (`patient_id`),
  KEY `fk_staff_id_idx` (`issued_by`),
  KEY `fk_doctor_id_idx` (`doctor_id`),
  KEY `fk_status_receipt_idx` (`status_id`),
  CONSTRAINT `fk_doctor_receipt` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`),
  CONSTRAINT `fk_patient_receipt` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`),
  CONSTRAINT `fk_staff_receipt` FOREIGN KEY (`issued_by`) REFERENCES `staff` (`staff_id`),
  CONSTRAINT `fk_status_receipt` FOREIGN KEY (`status_id`) REFERENCES `receipt_status` (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt`
--

LOCK TABLES `receipt` WRITE;
/*!40000 ALTER TABLE `receipt` DISABLE KEYS */;
INSERT INTO `receipt` VALUES (2019898,101,1002,1003,'2024-12-27 01:55:09',1000,5),(7430726,101,1002,1003,'2024-12-27 00:22:07',1000,1),(12755363,101,1002,1001,'2024-12-22 15:27:42',1000,1),(18105268,101,1002,1003,'2024-12-27 00:19:48',1000,1),(20157160,101,1002,1003,'2024-12-27 01:57:26',1000,5),(20329359,101,1002,1001,'2024-12-22 15:27:58',1000,5),(20459632,101,1002,1001,'2024-12-22 00:00:00',1000,1),(34829352,101,1002,1003,'2024-12-27 00:27:55',1000,1),(38050998,101,1003,1003,'2024-12-27 07:16:06',1000,5),(47657666,101,1002,1003,'2024-12-27 01:58:43',1000,5),(47709744,101,1002,1001,'2024-12-22 00:00:00',1000,1),(52109801,101,1003,1001,'2024-12-22 15:25:57',1000,1),(58018950,101,1002,1001,'2024-12-22 15:27:35',1000,1),(65467108,101,1003,1003,'2024-12-27 13:12:49',7500,5),(66781085,101,1003,1001,'2024-12-22 00:00:00',1000,1),(74474109,101,1002,1001,'2024-12-22 15:27:32',1000,1),(74982271,101,1002,1001,'2024-12-22 00:00:00',1000,1),(77555259,101,1002,1001,'2024-12-22 00:00:00',1000,1),(77607546,101,1002,1003,'2024-12-27 01:56:06',1000,5),(86013883,101,1002,1003,'2024-12-27 02:04:16',1000,5),(99481663,101,1002,1001,'2024-12-22 15:27:44',1000,1);
/*!40000 ALTER TABLE `receipt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt_reports`
--

DROP TABLE IF EXISTS `receipt_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt_reports` (
  `receipt_id` int DEFAULT NULL,
  `report_id` int DEFAULT NULL,
  `status` varchar(45) DEFAULT 'Pending',
  `doctor_notes` text,
  KEY `fk_report_id_idx` (`report_id`),
  KEY `fk_receipt_report` (`receipt_id`),
  CONSTRAINT `fk_receipt_report` FOREIGN KEY (`receipt_id`) REFERENCES `receipt` (`receipt_id`),
  CONSTRAINT `fk_report_receipt` FOREIGN KEY (`report_id`) REFERENCES `report` (`report_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt_reports`
--

LOCK TABLES `receipt_reports` WRITE;
/*!40000 ALTER TABLE `receipt_reports` DISABLE KEYS */;
INSERT INTO `receipt_reports` VALUES (99481663,1,'Completed','Imeadeatly Need'),(99481663,2,'Completed','Imeadeatly Need'),(99481663,3,'Pending','Imeadeatly Need'),(99481663,3,'Pending',NULL),(38050998,1,'Pending','Test'),(38050998,1,'Pending','Test'),(38050998,1,'Pending','Test'),(38050998,2,'Pending','Test'),(38050998,3,'Pending','Test'),(65467108,1,'Completed','test');
/*!40000 ALTER TABLE `receipt_reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt_status`
--

DROP TABLE IF EXISTS `receipt_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt_status` (
  `status_id` int NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt_status`
--

LOCK TABLES `receipt_status` WRITE;
/*!40000 ALTER TABLE `receipt_status` DISABLE KEYS */;
INSERT INTO `receipt_status` VALUES (1,'Open'),(2,'Doctor Inprogress'),(3,'Lab Inprogress'),(4,'Payment Pending'),(5,'Complete');
/*!40000 ALTER TABLE `receipt_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report` (
  `report_id` int NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
INSERT INTO `report` VALUES (1,'MRI',NULL,1500),(2,'CT',NULL,2000),(3,'XRAY',NULL,2500);
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `role_id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'receptionist'),(2,'doctor'),(3,'radiologist'),(4,'cashier');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `staff_id` int NOT NULL AUTO_INCREMENT,
  `nic` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `password` text,
  `role_id` int DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `registerd_by` int DEFAULT NULL,
  `registerd_date` datetime DEFAULT NULL,
  PRIMARY KEY (`staff_id`,`nic`),
  KEY `fk_staff_role_idx` (`role_id`),
  CONSTRAINT `fk_staff_role` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1005 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1001,'975864123','Pubodha','pubba',1,'55c kalubowila',10000,'2024-12-22 00:00:00'),(1002,'968574851','Samitha','choka',2,'568/5b piliyandala road',10000,'2024-12-22 00:00:00'),(1003,'199900511332','Samitha Prabath','$2b$12$2pkC.cx5xxnS3Kwxl1ad6uGdfeeM/meRogkw6a9AEr.iQoACigm62',1,'badulla',11,'2024-12-20 00:00:00');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_phone`
--

DROP TABLE IF EXISTS `staff_phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_phone` (
  `staff_id` int NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  PRIMARY KEY (`staff_id`,`phone_number`),
  CONSTRAINT `fk_staff_phone` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`staff_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_phone`
--

LOCK TABLES `staff_phone` WRITE;
/*!40000 ALTER TABLE `staff_phone` DISABLE KEYS */;
INSERT INTO `staff_phone` VALUES (1003,'0987654321'),(1003,'1234567890');
/*!40000 ALTER TABLE `staff_phone` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-27 14:32:58
