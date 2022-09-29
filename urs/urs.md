
### User Requirements Specification Document
##### DIBRIS – Università di Genova. Scuola Politecnica, Software Engineering Course 80154


**VERSION : X.X**

**Authors**  
XXXX
YYYY

**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
| 1.0 | 29/09/22 | Sara Urdangaray |  |

# Table of Contents

1. [Introduction](#p1)
	1. [Document Scope](#sp1.1)
	2. [Definitios and Acronym](#sp1.2) 
	3. [References](#sp1.3)
2. [System Description](#p2)
	1. [Context and Motivation](#sp2.1)
	2. [Project Objectives](#sp2.2)
3. [Requirement](#p3)
 	1. [Stakeholders](#sp3.1)
 	2. [Functional Requirements](#sp3.2)
 	3. [Non-Functional Requirements](#sp3.3)
  
  

<a name="p1"></a>

## 1. Introduction

<a name="sp1.1"></a>

### 1.1 Document Scope
Spiegare come funziona il trasferimento dei dati tra Conti diversi

<a name="sp1.2"></a>

### 1.2 Definitios and Acronym


| Acronym				| Definition | 
| ------------------------------------- | ----------- | 
| CC | Conto Corrente |

<a name="sp1.3"></a>

### 1.3 References 
../esame.pdf
<a name="p2"></a>

## 2. System Description
un applicazione che permette al ciente di acedere ai propri conti visualizzare il saldo, visualizzare le ultime transazioni, effettuare e ricevere transazioni di denaro
<a name="sp2.15"></a>

### 2.1 Context and Motivation
Gestione di un CC
<a name="sp2.2"></a>

### 2.2 Project Obectives 
Lanciare una nuova applicazione per la gestione dei conti per l'utilizzo dei clienti
<a name="p3"></a>

## 3. Requirements

| Priorità | Significato | 
| --------------- | ----------- | 
| M | **Mandatory:**   |
| D | **Desiderable:** |
| O | **Optional:**    |
| E | **future Enhancement:** |

<a name="sp3.1"></a>
### 3.1 Stakeholders
Banche
Clienti delle banche
<a name="sp3.2"></a>
### 3.2 Functional Requirements 

| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 1.0 |  applicazione funzionante sia su IOS sia su Android |M|
| 1.0 |  accesso iniziale con le credenziali dell'utente |M|
| 1.0 |  connessione al sistema del conto corrente |M|
| 1.0 |  effettuare trasferimenti di denaro |M|
| 1.0 |  ricevere trasferimenti di denaro |M|
| 1.0 |  controllo della possibilità di invio del denaro secondo il saldo corrente |M|
| 1.0 | visualizzare operazioni effettuate con data |M|

<a name="sp3.3"></a>
### 3.2 Non-Functional Requirements 
 
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 1.0 | implementare interfaccia grafica |E|
| 1.0 | implementare un sistema di aiuto clienti nel caso di errore o qualora il cliente non riesca a capire come utilizzare l'applicazione al meglio|D|
