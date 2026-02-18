import time
import os
import sys

board =[]
q_position = []
count = 0

def baca_file(nama_input_file):
  board=[]
  try:
    with open(nama_input_file, 'r') as f:
      for line in f:
        row = list(line.strip().upper())
        if row:
          board.append(row)
    if not board:
      print(f"File '{nama_input_file}' kosong.")
      return None
    
    N = len(board)
    for r in range(N):
      if len(board[r]) != N:
        print(f"File '{nama_input_file}' tidak valid. Baris dan kolom harus memiliki panjang yang sama.")
        return None
      
    return board
  
  except FileNotFoundError:
    print(f"File '{nama_input_file}' tidak ditemukan.")
    return None

def live_update(current_perm, N):
  os.system('cls' if os.name == 'nt' else 'clear')

  output_str = ""
  for r in range(N):
    line= ""
    for c in range(N):
      if current_perm[r] == c:
        line += "#"
      else:
        line += board[r][c] + ""
    output_str += line + "\n"
  print(output_str)
  time.sleep(0.1)

def validate(perm, N):
  used_colors = set()

  for r in range(N):
    c = perm[r]
    warna = board[r][c]
    if warna in used_colors:
      return False
    used_colors.add(warna)

  for r1 in range(N):
    for r2 in range(r1 + 1, N):
      c1 = perm[r1]
      c2 = perm[r2]
      if abs(r1 - r2) == abs(c1 - c2):
        if abs(r1 - r2) == 1:
          return False
  return True

def permute(arr, start_idx, end_idx):
  global count, q_position

  if start_idx == end_idx:
    count += 1
    current_comb = list(arr)

    q_position = current_comb

    if count % 100 == 0:
      live_update(current_comb, len(board))

    if validate(current_comb, len(board)):
      live_update(current_comb, len(board))
      return True
    return False
  
  for i in range (start_idx, end_idx + 1):
    arr[start_idx], arr[i] = arr[i], arr[start_idx]
    if permute(arr, start_idx + 1, end_idx):
      return True
    arr[start_idx], arr[i] = arr[i], arr[start_idx]
  return False

def save_file(nama_output_file, durasi, status, N):
  try:
    with open(nama_output_file, 'w') as f:
      if status:
        f.write("Solusi ditemukan:\n")
      else:
        f.write("Solusi tidak ditemukan:\n")
      for r in range(N):
        line = ""
        for c in range(N):
          if q_position[r] == c:
            line += "#"
          else:
            line += board[r][c] + ""
        f.write(line + "\n")    
      f.write(f"\nWaktu pencarian: {durasi:.4f} ms\n")
      f.write(f"Banyak kasus yang ditinjau: {count} kasus\n")
    print(f"Solusi berhasil disimpan ke '{nama_output_file}'.")
  except Exception as e:
    print(f"Gagal menyimpan solusi ke '{nama_output_file}'.")

input_file = input("Masukkan nama file: ")
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
test_folder = os.path.join(project_dir, 'test')
full_path = os.path.join(test_folder, input_file)
board_data = baca_file(full_path)

if board_data:
  board = board_data
  N = len(board)
  initial_arr = list(range(N))
  start_time = time.perf_counter()
  ketemu = permute(initial_arr, 0, N - 1)
  end_time = time.perf_counter()
  durasi = (end_time - start_time) * 1000

  os.system('cls' if os.name == 'nt' else 'clear')
  if ketemu:
    print("Solusi ditemukan:")
  else:
    print("Solusi tidak ditemukan:")
  for r in range(N):
    line = ""
    for c in range(N):
      if q_position[r] == c:
        line += "#"
      else:
        line += board[r][c] + ""
    print(line)
  print(f"\nWaktu pencarian: {durasi:.4f} ms")
  print(f"Banyak kasus yang ditinjau: {count} kasus")

  simpan = input("Apakah Anda ingin menyimpan solusi? (y/n): ").lower()
  if simpan == 'y':
    output_file = input("Masukkan nama file output: ")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    test_folder = os.path.join(project_dir, 'test')
    if not os.path.exists(test_folder):
      os.makedirs(test_folder)
    full_path = os.path.join(test_folder, output_file)
    save_file(full_path, durasi, ketemu, N)
  else:
    print("Solusi tidak disimpan.")

