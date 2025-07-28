<p align="center">
  <picture>
    <img alt="Генератор Криптографических Ключей" src="figures/logo.png" width="50%">
  </picture>
</p>

<h1 align="center">Генератор Криптографических Ключей</h1>

[![Build Status](https://img.shields.io/badge/Сборка-Успешна-brightgreen)](https://github.com/KoTiRiKi/crypto-keypair-generator/actions) [![License](https://img.shields.io/badge/Лицензия-MIT-blue.svg)](LICENSE)

## ⚠️ Важное уведомление

Если вы используете этот скрипт для генерации ключей, убедитесь, что ваши мнемонические фразы соответствуют стандарту BIP-39. Недопустимые или неполные фразы могут привести к ошибкам или небезопасным ключам. Используйте в безопасной, офлайн-среде. Никогда не делитесь приватными ключами.

## 📰 Новости

- 📅 **[28.07.2025 13:59 CEST]** Первый релиз Crypto Keypair Generator на GitHub!

## 🔭 Обзор

Скрипт **Crypto Keypair Generator** на Python позволяет генерировать ключевые пары Ethereum (EVM) и Solana из мнемонических фраз BIP-39. Поддерживаются различные операции: получение приватных ключей и адресов для EVM и Solana, с сохранением результатов в текстовые файлы.

> **Предупреждение:** Скрипт обрабатывает чувствительные криптографические данные. Используйте на свой страх и риск.

## 🚀 Возможности

- ✅ Генерация приватных ключей EVM из мнемоники
- ✅ Генерация адресов EVM из мнемоники или приватных ключей
- ✅ Генерация приватных ключей Solana из мнемоники
- ✅ Генерация адресов Solana из мнемоники
- ✅ Чтение мнемоники из файла `mnemonics.txt`, сохранение результатов

## 📦 Требования

Установите зависимости из `requirements.txt`:

```bash
pip install -r requirements.txt
```

| Пакет         | Версия   |
| ------------- | -------- |
| `eth-account` | Последняя |
| `mnemonic`    | Последняя |
| `bip-utils`   | >= 2.9.0 |
| `base58`      | Последняя |

## 📋 Установка

```bash
python -m venv venv
```

Активация виртуального окружения:

- **Windows**:

```bash
venv\Scriptsctivate
```

- **macOS/Linux**:

```bash
source venv/bin/activate
```

Клонируйте репозиторий:

```bash
git clone https://github.com/KoTiRiKi/crypto-keypair-generator.git
cd crypto-keypair-generator
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## 🎮 Использование

Создайте файл `mnemonics.txt` в директории проекта. Введите одну или несколько мнемонических фраз BIP-39, по одной в строке.

Пример:
```
retire fashion finish extend loop situate version picnic paddle sibling earn humor
```

Запуск скрипта:

```bash
python seed_to_private_evm_solana.py
```

Выберите действие (1–5):

1. Приватные ключи EVM → `private_keys_evm.txt`
2. Адреса EVM из приватных ключей → `addresses_evm.txt`
3. Адреса EVM из мнемоники → `addresses_evm.txt`
4. Приватные ключи Solana → `private_keys_solana.txt`
5. Адреса Solana → `addresses_solana.txt`

## 💡 Пример

Если в `mnemonics.txt`:
```
retire fashion finish extend loop situate version picnic paddle sibling earn humor
```
И выбрать опцию 3, будет сгенерирован адрес EVM и сохранён в `addresses_evm.txt`.

## 🔒 Безопасность

- Никогда не публикуйте `private_keys_evm.txt`, `private_keys_solana.txt`, `mnemonics.txt`
- Используйте скрипт в офлайн-среде
- Удаляйте вывод после использования вручную

## 🤝 Вклад

Приветствуются любые pull request'ы и предложения через Issues!

## 📜 Лицензия

Проект распространяется по лицензии **MIT**. Подробнее в [LICENSE](LICENSE).
