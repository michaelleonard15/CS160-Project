# These values are extracted from the database origin_ids
# SELECT DISTINCT source_id FROM agreements

valid_origins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25,
                 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
                 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
                 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
                 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138,
                 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]

# These values are extracted from the database target_ids
# SELECT DISTINCT target_id FROM agreements ORDER BY target_id
valid_destinations = [7, 11, 12, 21, 23, 26, 29, 39, 42, 46, 50, 60, 75, 76, 79, 81,
                      88, 89, 115, 116, 117, 120, 128, 129, 132, 141, 143, 144]
