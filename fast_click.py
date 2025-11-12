import pyautogui
import time
import sys

def get_position():
    """マウスの現在位置を取得する関数"""
    print("\nクリックする位置にマウスを移動させてください")
    print("位置が決まったらEnterキーを押してください...")
    print("中断するにはCtrl+Cを押してください")

    try:
        input()  # Enterキーが押されるのを待つ
        pos = pyautogui.position()
        print(f"\n座標を取得しました: X={pos.x}, Y={pos.y}")
        return pos
    except KeyboardInterrupt:
        print("\n処理を中断しました。")
        sys.exit(0)

def main():
    print("=== マウスクリック自動化ツール ===")

    # 実行時間（秒数）の取得
    while True:
        try:
            duration_seconds = float(input("\n実行時間を秒数で入力してください: "))
            if duration_seconds > 0:
                break
            print("0より大きい数値を入力してください。")
        except ValueError:
            print("有効な数値を入力してください。")

    # 設定内容を表示
    print(f"\n=== 設定内容 ===")
    print(f"実行時間: {duration_seconds}秒")
    print("最速でクリックを実行します")
    print("================")

    # クリック位置の取得（最後に取得）
    position = get_position()

    # 即時実行
    print("\nクリックを開始します。終了するにはマウスを画面の端に移動させるか、Ctrl+Cを押してください。")

    pyautogui.PAUSE = 0  # 各操作間の待機時間を0に設定
    pyautogui.FAILSAFE = True  # マウスを画面の端に移動させると緊急停止
    start_time = time.time()  # 処理開始時間を記録
    end_time = start_time + duration_seconds  # 終了時刻を計算
    click_count = 0  # クリック回数をカウント
    last_print_time = start_time  # 最後に進捗を表示した時間

    try:
        print("\r", end="")  # 最初の改行を防ぐ
        while time.time() < end_time:
            pyautogui.click(position)
            click_count += 1

            # 進捗表示（0.1秒ごと）
            current_time = time.time()
            if current_time - last_print_time >= 0.1:  # 0.1秒ごとに表示
                elapsed = current_time - start_time
                remaining = max(0, end_time - current_time)
                cps = click_count / elapsed if elapsed > 0 else 0
                print(f"\r経過: {elapsed:.1f}秒 / 残り: {remaining:.1f}秒 | "
                      f"合計クリック数: {click_count:,}回 | "
                      f"CPS: {cps:,.1f}", end="")
                last_print_time = current_time

    except KeyboardInterrupt:
        print("\n\n処理がユーザーによって中断されました。")
    except pyautogui.FailSafeException:
        print("\n\nマウスが画面の端に移動したため、処理を中断します。")
    except Exception as e:
        print(f"\n\nエラーが発生しました: {e}")
    finally:
        total_time = time.time() - start_time
        print(f"\n=== 実行結果 ===")
        print(f"合計クリック回数: {click_count:,}回")
        print(f"合計実行時間: {total_time:.2f}秒")
        if total_time > 0:
            print(f"平均CPS: {click_count / total_time:,.1f}回/秒")
        print("================")
        print("\n処理を終了しました。")

if __name__ == "__main__":
    main()
