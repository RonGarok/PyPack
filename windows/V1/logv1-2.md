# 🐞 Bug Report – Blocage de PyPackV1.exe par Windows Defender  
# 🐞 Bug Report – PyPackV1.exe Blocked by Windows Defender

**📅 Release of the log :** 15/01/26  
**📦 New Version provided at maximum :** 20/01/26  

---

# 🇫🇷 Version Française

## 🔎 1. Description du problème

Sur certains systèmes Windows, **PyPackV1.exe est bloqué par l’antivirus intégré (Windows Defender)**.  
Le message d’erreur indique que le fichier contient un **virus ou un logiciel potentiellement indésirable**, empêchant toute exécution.

**Chemin concerné :**  
`C:\Users

\[NomUtilisateur]\Downloads\PyPackV1.exe`

**Message affiché :**  
> Impossible de terminer l'opération, car le fichier contient un virus ou un logiciel potentiellement indésirable.

---

## 🧪 2. Analyse technique

- Le fichier est détecté comme potentiellement dangereux par Windows Defender.
- Aucun comportement malveillant n’a été identifié dans le fonctionnement de PyPackV1.
- Le blocage semble lié :
  - à la méthode d’emballage utilisée pour l’exécutable,
  - à l’absence de signature numérique,
  - ou à des heuristiques trop agressives du moteur antivirus.

---

## 🛠️ 3. Contournements proposés

- Utiliser un autre antivirus ou désactiver temporairement la protection en temps réel (⚠️ à vos risques).
- Déplacer le fichier dans un répertoire non surveillé.
- Lancer l’exécutable via PowerShell ou CMD avec élévation.
- Fournir une version alternative `.zip` contenant les fichiers nécessaires à l’exécution manuelle.

---

## ✅ 4. Conclusion

Le blocage de PyPackV1.exe par Windows Defender empêche son utilisation sur certains systèmes.  
Une version corrigée est en cours de préparation et sera publiée **au plus tard le 20/01/26**.

---

# 🇬🇧 English Version

## 🔎 1. Issue Description

On some Windows systems, **PyPackV1.exe is blocked by the built-in antivirus (Windows Defender)**.  
The error message states that the file contains a **virus or potentially unwanted software**, preventing execution.

**Affected path:**  
`C:\Users

\[Username]\Downloads\PyPackV1.exe`

**Displayed message:**  
> Operation cannot be completed because the file contains a virus or potentially unwanted software.

---

## 🧪 2. Technical Analysis

- The file is flagged as potentially harmful by Windows Defender.
- No malicious behavior has been observed in PyPackV1’s runtime.
- The block appears related to:
  - the packaging method used for the executable,
  - lack of digital signature,
  - or overly aggressive heuristic detection.

---

## 🛠️ 3. Suggested Workarounds

- Use a different antivirus or temporarily disable real-time protection (⚠️ at your own risk).
- Move the file to a non-monitored folder.
- Launch the executable via PowerShell or CMD with elevation.
- Provide an alternative `.zip` version with manually executable files.

---

## ✅ 4. Conclusion

The blocking of PyPackV1.exe by Windows Defender prevents usage on some systems.  
A fixed version is being prepared and will be released **no later than 20/01/26**.

