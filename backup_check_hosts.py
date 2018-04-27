
import sys
import csv

def main():

    print("Backup hosts (all) : `%s`"%(sys.argv[1]))
    print("Supported hosts : `%s`"%(sys.argv[2]))

    missingHosts_list = []
    missingHosts_sum = 0

    allHosts_sum = 0

    allHosts_fname = sys.argv[1]
    supHosts_fname = sys.argv[2]
    allHosts_csvReader = csv.reader(open(allHosts_fname,'r'))
    supHosts_csvReader = csv.reader(open(supHosts_fname,'r'))
    allHosts_list = []

    for allHosts_row in allHosts_csvReader :
        allHosts_tmprow = allHosts_row
        allHosts_tmprow[0] = allHosts_tmprow[0].lower()
        allHosts_list.append(allHosts_tmprow[0])
        # print("allhosts row : %s"%(allHosts_row))
        allHosts_sum += 1

    print(":::All hosts : %d :::"%(allHosts_sum))

    for supHosts_row in supHosts_csvReader :
        currentSupHost = supHosts_row
        currentSupHost[0] = currentSupHost[0].lower()
        if currentSupHost[0] in allHosts_list:
            continue
        else:
            print(":::WARNING :"+currentSupHost[0]+" is missing")
            missingHosts_sum += 1
            missingHosts_list.append(currentSupHost)

    print("missing hosts : %d"%missingHosts_sum)
    print(':::missing hosts list : ')
    print(missingHosts_list)

    with open('results.csv','w') as myfile:
        for entries in missingHosts_list:
            myfile.write("%s, %s\n"%(entries[0],entries[1]))

        # wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
`        # wr.writerow(missingHosts_list)









    #
    # if missingHosts_sum == 0:
    #     print('::: No missing hosts :::')
    # else:
    #     print("::: Missing hosts : %d out of %d :::"%(missingHosts_sum,supHosts_sum))
    #     print(missingHosts_list)


if __name__ == "__main__":
    main()