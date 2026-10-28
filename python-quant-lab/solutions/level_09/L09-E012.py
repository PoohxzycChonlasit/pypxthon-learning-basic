def reject_negative_test_result(values):
    return 'continue' if values and sum(values)/len(values)>0 else 'reject'
