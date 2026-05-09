import time

class Timer:
    """with bloki qancha vaqt ishlashini o'lchaydi."""
    def __init__(self, label=""):
        self.label = label

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self._start
        print(f"  [{self.label}] {self.elapsed:.4f} sek")

class TempFile:
    """Foydalanilgandan keyin faylni o'chiradi."""
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.f = open(self.name, "w")
        return self.f

    def __exit__(self, exc_type, *args):
        self.f.close()
        import os; os.remove(self.name)
        if exc_type:
            print(f"  Xato bo'ldi, fayl o'chirildi: {self.name}")
        return False

if __name__ == "__main__":
    with Timer("ro'yxat yaratish"):
        total = sum(i**2 for i in range(100_000))
    print("  Natija:", total)

    with TempFile("temp.txt") as f:
        f.write("Vaqtinchalik ma'lumot")
    print("  TempFile yopildi va o'chirildi.")
