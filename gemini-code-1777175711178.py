import math

def calculate_busking_income():
    print("--- 街頭藝人收入計算系統 ---")
    
    # 1. 輸入數據
    total_revenue = float(input("1. 請輸入今日總收入: "))
    gas_cost = float(input("2. 請輸入車油錢: "))
    kerosene_drums = int(input("3. 請輸入煤油桶數 (一桶 262 元): "))
    cleaning_oil_bottles = int(input("4. 請輸入去漬油罐數 (一罐 50 元): "))
    performer_count = int(input("5. 請輸入表演者總人數: "))

    # 運算燃料費
    # 煤油錢：262 * 桶數，四捨五入至百位
    raw_kerosene_cost = kerosene_drums * 262
    kerosene_cost = round(raw_kerosene_cost / 100) * 100
    
    # 去漬油錢：50 * 罐數，四捨五入至百位
    raw_cleaning_oil_cost = cleaning_oil_bottles * 50
    cleaning_oil_cost = round(raw_cleaning_oil_cost / 100) * 100

    # 計算剩餘可分配金額 (總額 - 車油 - 煤油 - 去漬油)
    remaining_after_costs = total_revenue - gas_cost - kerosene_cost - cleaning_oil_cost

    # 邏輯判斷：如果每人平均不到 500 元，則不收團費
    temp_avg = remaining_after_costs / performer_count if performer_count > 0 else 0
    
    if temp_avg < 500:
        group_fee = 0
    else:
        # 團費：剩餘金額抽一成
        group_fee = remaining_after_costs * 0.1

    # 計算每人應分得金額 (扣除團費後平分，並四捨五入到百位)
    # 此金額必須為整數，方便現場發錢
    amount_for_distribution = remaining_after_costs - group_fee
    per_person_pay = round((amount_for_distribution / performer_count) / 100) * 100
    
    # 關鍵規則：平分後的差額與小數點，全部由團費吸收/調整
    # 實際發出的總人頭費
    total_person_payout = per_person_pay * performer_count
    # 最終團費 = 剩餘總額 - 實際發出去的人頭費
    final_group_fee = remaining_after_costs - total_person_payout

    # 顯示結果
    print("\n" + "="*30)
    print(f"【計算結果】")
    print(f"1. 車油錢: {gas_cost:.0f} 元")
    print(f"2. 煤油錢 (已捨入): {kerosene_cost} 元")
    print(f"3. 去漬油錢 (已捨入): {cleaning_oil_cost} 元")
    print("-" * 20)
    print(f"4. 團費 (包含餘數調整): {final_group_fee:.0f} 元")
    print(f"5. 每位表演者分得: {per_person_pay} 元 (共 {performer_count} 人)")
    print("="*30)

if __name__ == "__main__":
    calculate_busking_income()