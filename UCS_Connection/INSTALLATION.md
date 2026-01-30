# Techn. Hinweise für UCS-Betreiber zur Nutzung des neuen BILDUNGSLOGIN-Lizenzmanagers

BILDUNGSLOGIN bietet eine neue Lizenzverwaltung an, die im Zusammenspiel mit UCS nutzbar ist.

Hinweise zur **Nutzungsvereinbarung** und den entstehenden **Kosten** sowie eine Beschreibung der **Funktionen der neuen Lizenzverwaltung** finden Sie [hier.](https://info.bildungslogin.de/dienste/tutorials/onboarding-univention) Bei Fragen zur Installation und der Nutzungsvereinbarung wenden Sie sich bitte an service@bildungslogin-support.de. 

## I. Nutzung der neuen Lizenzverwaltung als SaaS

Die neue Lizenzverwaltung von BILDUNGSLOGIN basiert auf einer modernen Architektur mit Frontend/Backend, die containerisiert betrieben wird. Dieser Aufbau ermöglicht einen eigenständigen Betrieb als Teil einer IT-Infrastruktur mit ucs@school durch einen Träger.

Aufgrund der Erfahrung der letzten Jahre macht ein eigenständiger Betrieb aber erst ab einer Schulanzahl > 150 Schulen pro Träger Sinn. Sind weniger Schulen eines Trägers über das IDAM-System an die Lizenzverwaltung anzuschließen, bietet BILDUNGSLOGIN die Nutzung der Lizenzverwaltung als SaaS-Dienst an. Dieser wird über Standardschnittstellen angebunden und ist damit vergleichbar zum Medienregal von BILDUNGSLOGIN.

Die Nutzung des Univention ID-Brokers ist nicht möglich, da nicht alle notwendigen Attribute der Schulstrukturdaten für eine effiziente Lizenzverwaltung übertragen werden können.


An der Nutzung des BILDUNGSLOGIN-Medienregals ändert sich durch die neue Lizenzverwaltung nichts.

## II. Vorbereitung der Nutzung

Um die neue Lizenzverwaltung als SaaS zu nutzen, sind einige vorbereitende Schritte in Abstimmung mit BILDUNGSLOGIN erforderlich:

### 1\. SSO-Anbindung via OIDC

Die Anmeldung an der neuen Lizenzverwaltung erfolgt über OIDC. Dies wird UCS-seitig via Keycloak unterstützt (siehe [Infos zur **UCS-Keycloak-App**](https://www.univention.com/blog-en/2024/06/univention-app-highlights-keycloak/)). Falls Sie Unterstützung bei der Konfiguration der Keycloak-App in UCS benötigen, wenden Sie sich bitte an den Univention-Support, BILDUNGSLOGIN kann dafür keinen Support leisten.

Für den **Austausch der OIDC-Konfigurationsdaten** erhalten Sie von BILDUNGSLOGIN Zugang zu einem Konfigurationsdatenblatt. Nachdem Sie Ihre Anbindungsdaten dort hinterlegt haben, wird BILDUNGSLOGIN die SSO-Anbindung in zeitlicher Abstimmung mit Ihnen entsprechend konfigurieren.

#### Zusätzliche Claims in OIDC-Tokens

Zusätzlich zur Nutzer-ID ("preferred_username") ist:
- die **Übermittlung der UCS-School-ID** in OIDC-Claims obligatorisch. Siehe [Details](OIDC-mapper.md#hinzufügen-des-claims-ucsschoolschool) zur Konfiguration des Claims ucsschoolSchool, und
- die **Übermittlung von Gruppen** in OIDC-Claims notwendig, um die Nutzer an der Lizenzverwaltung bzw. beim Medienregal zu autorisieren. Siehe [Details](OIDC-mapper.md#hinzufügen-des-claims-ucsschoolgroups) zur Konfiguration des Claims ucsschoolGroups.

Die komplette Konfiguration der Clients sowie Mapper finden Sie unter [Details zur Konfiguration](https://github.com/BILDUNGSLOGIN/lizenzmanager_ucs/blob/main/OIDC-mapper.md).

### 2\. Einrichtung der Schulstrukturdaten-Provisionierung über die Kelvin-API

Der neue BILDUNGSLOGIN-Lizenzmanager ruft die **Schulstrukturdaten inkl. aller Nutzerdaten** bei jedem Login eines Lizenz-Admins aus UCS ab. Dies erfolgt über die [**Kelvin-API**](https://docs.software-univention.de/ucsschool-kelvin-rest-api/index.html). Es ist deshalb eine Installation/**Einrichtung der Kelvin-API** erforderlich.

Die Konfigurationsdaten hierfür werden ebenfalls über das BILDUNGSLOGIN-Konfigurationsdatenblatt übermittelt und anschließend die Anbindung von BILDUNGSLOGIN entsprechend konfiguriert.

Bitte beachten Sie, dass der neue Lizenzmanager über die API **nur User mit den Rollen "student" (Schüler/in) oder "teacher" (Lehrkraft)** abruft, aber keine User mit der Rolle "staff" (Mitarbeiter). Falls User mit der Rolle "staff" in Ihrem UCS-System Lizenzen zugewiesen haben, sorgen Sie bitte dafür, dass diese mindestens auch noch eine der beiden anderen Rollen besitzen. Andernfalls können diese Lizenzen nicht migriert und im neuen Lizenzmanager nicht genutzt werden.


### 3\. Konfiguration des Admin-Zugriffs auf die neue Lizenzverwaltung

Der Admin-Zugang zur neuen Lizenzverwaltung erfolgt per SSO über autorisierte Accounts in UCS. User, die Zugriff auf die Lizenzverwaltung erhalten sollen, müssen einer neu zu erstellenden **Gruppe unterhalb der jeweiligen Schul-OU mit den Gruppennamen _bilo_lizenzadmins-<Schulkürzel>_** zugeordnet sein, wobei _<Schulkürzel>_ durch den Wert des Feldes "Schulkürzel" (nicht: "Name der Schule") in UCS zu ersetzen ist.
(Für die automatische Erstellung dieser Gruppen bei UCS-Instanzen mit mehreren Schulen steht [ein Skript zur Verfügung](tools/create_license_admin_groups.py)).

**Wichtig:** Eine von Accounts mit der Rolle "Schul-Admin" alleine genügt für die Autorisierung nicht; vielmehr ist es auf dem beschriebenen Weg auch möglich, Accounts ohne Schul-Admin-Rolle für die Nutzung der Lizenzverwaltung zu autorisieren.

Für für den Zugang zur neuen BILDUNGSLOGIN-Lizenzverwaltung erstellen Sie eine **neue Portal-Kachel** mit Berechtigungen für Schul-Admins. Das Icon für die Kachel und den zu hinterlegenden Link für den Aufruf der neuen externen Lizenzverwaltung erhalten Sie von BILDUNGSLOGIN.

### 4\. Deaktivierung der Kerberos- Authentifizierung

Normalerweise erfolgt die Authentifizierung von Diensten ausschließlich über OIDC. Da die Kerberos-Authentifizierung bei einigen Browsern zu Problemen führen kann, kann diese deaktiviert werden - soweit diese nicht für andere Dienste verwendet werden muss. Siehe [Details zur Deaktivierung der Kerberos-Authentifizierung](KERBEROS.md).
