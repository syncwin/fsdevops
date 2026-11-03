#!/usr/bin/env bash
set -e
mkdir -p lib/settings test
cat > pubspec.yaml <<'EOF'
name: demo_app
environment:
  sdk: ^3.9.0
dependencies:
  flutter:
    sdk: flutter
  provider: ^6.1.0
dev_dependencies:
  flutter_lints: ^6.0.0
EOF
echo 'include: package:flutter_lints/flutter.yaml' > analysis_options.yaml
cat > lib/main.dart <<'EOF'
import 'package:flutter/material.dart';
import 'settings/settings_screen.dart';

void main() => runApp(const MaterialApp(home: SettingsScreen()));
EOF
cat > lib/settings/settings_screen.dart <<'EOF'
import 'package:flutter/material.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});
  static Map<String, String>? prefs;
  @override
  Widget build(BuildContext context) {
    final apiKey = 'demo-hardcoded-api-key';
    return Scaffold(body: Text(prefs!['theme']! + apiKey));
  }
}
EOF
git init -q && git add -A && git -c user.email=e@e -c user.name=e commit -qm init
