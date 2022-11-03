# slack-backup-token-inserter
This Python script is used to fix missing files after exporting Slack channels using https://github.com/mrmoneyc/slack-exporter

## Usage
### Configuring `slack-exporter`
To use this Python scrypt it's convenient to set `slack-exporter` `config.yaml` variables like that:
```
<...>
SplitMessages: false
ArchiveData: false
DownloadFiles: false
<...>
```

### Creating `xoxe` file export token
1. Go to https://slack.com/services/import
2. Create any date range export. It's better to choose 7 days to make it fater
3. Open any `.json` file in `<channel-name>` folder wich contains any attachements
4. Find (using ctrl+F) your `xoxe` token and save it

### Running slack-backup-token-inserter
1. Export any channel using https://github.com/mrmoneyc/slack-exporter and set `config.yaml` variables like above
2. Clone `main.py`
3. Install Python 3
4. Find the `messages.json` file which you want to update
5. Run `main.py` using your 'xoxe` token via 
```
python main.py "?t=xoxe-123-456-789" ./messages.json ./new-messages.json
```
6. Delele `messages.json` and rename `new-messages.json` to `messages.json`
7. Create `.zip` archive using the whole folder witch contains
```
<channel-name-folder>
users.json
channels.json
```
