---
title: "Why the secrets Module is the Ideal Choice for Generating Random Strings in Python"
date: 2023-04-08T09:58:01+08:00
---

以前就一直很愛用 ruby 提供的 [securerandom](https://ruby-doc.org/stdlib-2.5.1/libdoc/securerandom/rdoc/SecureRandom.html) 來產生隨機字串，

但之前長時間使用 Python2 進行開發，一直忽略了 Python3 應該也會有類似的 module，

直到昨天有需求又查了一下發現，ㄏㄏ早在 3.6 就有提供這個 module 了，試一下跟 [securerandom](https://ruby-doc.org/stdlib-2.5.1/libdoc/securerandom/rdoc/SecureRandom.html) 87% 像，推薦給大家

簡單來說用 `secrets` 的好處是比起傳統 `random` module 產生出來的隨機字串
- 更具有密碼學上的安全性
- 更快，更簡單可以產生字串


原理的話其實就是用 [os.urandom](https://docs.python.org/3/library/os.html#os.urandom)
取代 [random module](https://docs.python.org/3/library/os.html#os.urandom) 內的擬隨機演算法


```python
# 偷懶版本，要注意 32 是 bytes，實際產生出來的長度因為 base64 encode 的關係會超過 32
from secrets import token_urlsafe
print(token_urlsafe(32))

# 長一點的版本，使用 secrets.choice
import secrets import string
alphabet = string.ascii_letters + string.digits
random_string = ''.join(secrets.choice(alphabet) for i in range(16))
print(random_string)
```


## ChatGPT 的回答
```bash
The benefits of using the secrets module to generate random strings (and other values) over the random module are:

Cryptographic security: The secrets module uses a cryptographically secure random number generator provided by the operating system, which is designed to be resistant to prediction and manipulation. The random module, on the other hand, uses a simpler algorithm that is not intended for cryptographic use.

Convenience: The secrets module provides a simple and intuitive interface for generating random values, without requiring manual seeding or other setup.

Efficiency: The secrets module is optimized for generating large amounts of random data quickly, and can generate random strings and other values much faster than the random module.
```


## References
- https://peps.python.org/pep-0506/
- https://docs.python.org/3/library/secrets.html
- [source code](https://github.com/python/cpython/blob/main/Lib/secrets.py)
