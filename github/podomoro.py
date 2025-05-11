import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ {time_format}", end="")
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Waktu habis!\n")

def pomodoro():
    print("=== POMODORO TIMER ===")

    work_time = int(input("⏱️ Masukkan waktu kerja (menit): "))
    short_break = int(input("🧘 Masukkan waktu short break (menit): "))
    long_break = int(input("🛌 Masukkan waktu long break (menit): "))

    while True:
        print("\nMode:\n1. Kerja\n2. Short Break\n3. Long Break\n4. Keluar")
        choice = input("Pilih mode (1/2/3/4): ")

        if choice == "1":
            print(f"\nMulai kerja selama {work_time} menit...\n")
            countdown(work_time)
        elif choice == "2":
            print(f"\nShort break selama {short_break} menit...\n")
            countdown(short_break)
        elif choice == "3":
            print(f"\nLong break selama {long_break} menit...\n")
            countdown(long_break)
        elif choice == "4":
            print("👋 Keluar dari Pomodoro Timer.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    pomodoro()
