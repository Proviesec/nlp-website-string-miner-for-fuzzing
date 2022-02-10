# NLP Website string miner for fuzzing

Find all keywords for your subdomain or folder search with website scrapping and NLP - for FUZZ (Bug Bounty)

<a href="https://proviesec.org/">
    <img src="https://avatars.githubusercontent.com/u/92156402?s=400&u=7fe0dbb9085a37818ee8c2b061432a9a69cbff42&v=4" alt="Proviesec logo" title="Proviesec" align="right" height="60" />
</a>
<a href="https://www.buymeacoffee.com/proviesec" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Installation
------------

1. git clone https://github.com/Proviesec/nlp-website-string-miner-for-fuzzing.git
2. cd nlp-website-string-miner-for-fuzzing
3. pip install -r requirements.txt or pip3 install -r requirements.txt


Documentation / Tutorials
-------------

- Deep: says how many levels (links) should be followed. Deep 2 says: all links from the first page and all links present on the next pages are viewed.
- ![image](https://user-images.githubusercontent.com/6010786/145686516-11770d5b-a21e-4427-99d8-d1a0ba2c5991.png)

# Example:
Screen:


py -3 .\dir-name-crawler.py http://github.com       
Output:
``` {'longer', 'contributors', 'twitter', 'octopus', 'enhance', 'javascript', 'secrets', 'partners', 'discussions', 'ohmyzshohmyzsh', 'laptops', 'actions', 'tensorflow', 'dev', 'conflicts', 'support', 'emptybody', 'flow', 'month', 'zero', 'maintain', 'swift', 'repo', 'octocat', 'arm', 'press', 'collaboration', 'jobs', 'zsh', 'cat', 'browser', 'requests', 'ship', 'contribution', 'fortune', 'efficient', 'codespaces', 'react', 'linkedin', 'npm', 'fields', 'software', 'addstatusscreens', 'infrastructure', 'core', 'system', 'eslint', 'plans', 'delightful', 'mag', 'story', 'environment', 'record', 'builds', 'space', 'jump', 'operating', 'topics', 'keeps', 'github', 'atom', 'help', 'kuberneteskubernetes', 'services', 'experiment', 'confirmation', 'requestsconversations', 'jasonetcooctocatclassifier', 'accelerate', 'flutter', 'youtube', 'security', 'source', 'fix', 'program', 'anything', 'inclusion', 'customer', 'host', 'gh', 'desktop', 'automate', 'indexjs', 'secure', 'data', 'vault', 'ohmyzsh', 'company', 'rust', 'pull', 'propose', 'session', 'blog', 'productiongrade', 'sign', 'connect', 'integrations', 'impact', 'build', 'secret', 'voice', 'clicli', 'set', 'onthe', 'automation', 'organization', 'reviews', 'commits', 'stop', 'containers', 'rewind', 'githubthe', 'cloud', 'kubernetes', 'language', 'control', 'handle', 'search', 'rustlangrust', 'heart', 'companies', 'repository', 'privacy', 'depend', 'sync', 'remote', 'install', 'oauth', 'someone', 'paid', 'container', 'hashicorpterraform', 'vm', 'world', 'gatsbyjsgatsby', 'development', 'technologies', 'value', 'input', 'interfaces', 'details', 'sales', 'fast', 'service', 'choice', 'web', 'sponsors', 'tokens', 'puts', 'joshaber', 'macos', 'explore', 'repositories', 'classifier', 'terms', 'simple', 'questions', 'create', 'readme', 'minutes', 'production', 'tensorflowtensorflow', 'conversations', 'thanks', 'funding', 'passing', 'days', 'machine', 'management', 'scale', 'careers', 's', 'vulnerability', 'user', 'desire', 'apps', 'confirmations', 'building', 'tests', 'small', 'check', 'contributions', 'jasonetco', 'flutterflutter', 'homeassistantcore', 'risk', 'developer', 'declarative', 'merge', 'partner', 'branch', 'tab', 'keys', 'stars', 'number', 'developers', 'team', 'site', 'terraform', 'enables', 'gatsby', 'bugs', 'depends', 'top', 'installation', 'home', 'resources', 'enterprise', 'events', 'change', 'others', 'forum', 'ci', 'issues', 'current', 'appleswift', 'compare', 'share', 'review', 'community', 'organizations', 'steps', 'shop', 'vulnerabilities', 'stories', 'marketplace', 'lab', 'date', 'setup', 'cli', 'beautiful', 'product', 'matrix', 'identifies', 'everything', 'level', 'want', 'git', 'map', 'facebookreact', 'guides', 'window', 'api', 'pmarsceill', 'mobile', 'it', 'package', 'invalidate', 'browse', 'results', 'contact', 'size', 'ask', 'sophshep', 'fees', 'features', 'communitydriven', 'configuration', 'workflow', 'experiments', 'stickers', 'answer', 'reach', 'x', 'notify', 'roadmap', 'projects', 'refresh', 'environments', 'npmcli', 'blazing', 'found', 'library', 'changes', 'everyone', 'write', 'docs', 'packages', 'codebase', 'script', 'websites', 'place', 'photographs', 'project', 'public', 'work', 'token', 'manager', 'cover', 'inventions', 'matters', 'code', 'reload', 'squash', 'electron', 'teams', 'pr', 'player', 'platform', 'education', 'supports', 'suggestion', 'key', 'built', 'framework', 'profile', 'green', 'millions', 'octocatclassifier', 'status', 'windows', 'facebook', 'https', 'studio', 'starts', 'push', 'origin', 'request', 'checks', 'registry', 'collections', 'readmemd', 'octocats', 'contribute', 'fund'} ```

-------------
https://textblob.readthedocs.io/en/dev/install.html

# Disclaimer: DONT BE A JERK!
Needless to mention, please use this tool very very carefully. The authors won't be responsible for any consequences.
