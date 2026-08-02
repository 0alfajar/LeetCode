class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_digits = date.split('-')
        date_bins = []
        for date_bin in date_digits:
            date_bins.append(format(int(date_bin), 'b'))
        return f'{date_bins[0]}-{date_bins[1]}-{date_bins[2]}'