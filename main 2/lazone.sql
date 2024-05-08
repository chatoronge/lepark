-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 03 mai 2024 à 10:23
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `lazone`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

CREATE TABLE `admin` (
  `ID_admin` int(11) NOT NULL,
  `Nom` varchar(255) NOT NULL,
  `Prénom` varchar(255) NOT NULL,
  `Adresse_email` varchar(255) NOT NULL,
  `Mot_de_passe` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `catégories`
--

CREATE TABLE `catégories` (
  `ID` int(11) NOT NULL,
  `Nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `clients`
--

CREATE TABLE `clients` (
  `ID_client` int(11) NOT NULL,
  `Nom` varchar(255) NOT NULL,
  `Prénom` varchar(255) NOT NULL,
  `Adresse` varchar(255) NOT NULL,
  `Adresse_email` varchar(255) NOT NULL,
  `Mot_de_passe` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `clients`
--

INSERT INTO `clients` (`ID_client`, `Nom`, `Prénom`, `Adresse`, `Adresse_email`, `Mot_de_passe`) VALUES
(1, 'Doe', 'John', '123 Rue de la Poste', 'john.doe@example.com', 'mot_de_passe_1'),
(2, 'Smith', 'Jane', '456 Avenue du Soleil', 'jane.smith@example.com', 'mot_de_passe_2'),
(3, 'Garcia', 'Maria', '789 Boulevard des Fleurs', 'maria.garcia@example.com', 'mot_de_passe_3'),
(4, 'Brown', 'Michael', '1010 Rue de la Liberté', 'michael.brown@example.com', 'mot_de_passe_4'),
(5, 'Taylor', 'Emma', '111 Place de la Gare', 'emma.taylor@example.com', 'mot_de_passe_5');

-- --------------------------------------------------------

--
-- Structure de la table `produits`
--

CREATE TABLE `produits` (
  `id` int(100) NOT NULL,
  `modele` varchar(100) NOT NULL,
  `prix` varchar(255) NOT NULL,
  `stock` int(255) NOT NULL,
  `reference` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `produits`
--

INSERT INTO `produits` (`id`, `modele`, `prix`, `stock`, `reference`) VALUES
(1, 'Planche cool', '59.99', 10, 'REF001'),
(2, 'Normale', '69.99', 15, 'REF002'),
(3, 'Foot-Fetish', '79.99', 20, 'REF003'),
(4, 'Herman Signature', '89.99', 12, 'REF004'),
(5, 'Aixoise ', '99.99', 8, 'REF005');

-- --------------------------------------------------------

--
-- Structure de la table `produits_catégories`
--

CREATE TABLE `produits_catégories` (
  `ID_produit` int(11) NOT NULL,
  `ID_catégorie` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID_admin`);

--
-- Index pour la table `catégories`
--
ALTER TABLE `catégories`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`ID_client`);

--
-- Index pour la table `produits`
--
ALTER TABLE `produits`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `produits_catégories`
--
ALTER TABLE `produits_catégories`
  ADD PRIMARY KEY (`ID_produit`,`ID_catégorie`),
  ADD KEY `ID_catégorie` (`ID_catégorie`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID_admin` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `catégories`
--
ALTER TABLE `catégories`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `clients`
--
ALTER TABLE `clients`
  MODIFY `ID_client` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `produits`
--
ALTER TABLE `produits`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `produits_catégories`
--
ALTER TABLE `produits_catégories`
  ADD CONSTRAINT `produits_catégories_ibfk_1` FOREIGN KEY (`ID_produit`) REFERENCES `produits` (`id`),
  ADD CONSTRAINT `produits_catégories_ibfk_2` FOREIGN KEY (`ID_catégorie`) REFERENCES `catégories` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
