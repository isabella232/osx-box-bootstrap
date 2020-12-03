#schema of the table on Catalina 10.15.6
#
#CREATE TABLE access (
#  service        TEXT        NOT NULL,
#  client         TEXT        NOT NULL,
#  client_type    INTEGER     NOT NULL,
#  allowed        INTEGER     NOT NULL,
#  prompt_count   INTEGER     NOT NULL,
#  csreq          BLOB,
#  policy_id      INTEGER,
#  indirect_object_identifier_type    INTEGER,
#  indirect_object_identifier         TEXT,
#  indirect_object_code_identity      BLOB,
#  flags          INTEGER,
#  last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),
#  PRIMARY KEY (service, client, client_type, indirect_object_identifier),
#  FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);
sudo sqlite3 "/Library/Application Support/com.apple.TCC/TCC.db" "INSERT INTO access VALUES('kTCCServiceAccessibility','com.apple.dt.Xcode',0,1,1,'','','','UNUSED','',0,'1606910422');"
