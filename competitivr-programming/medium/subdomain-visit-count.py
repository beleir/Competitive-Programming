class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        graph = {}
        for i in cpdomains:
            v = i.find(" ")
            visits = int(i[:v])
            k = 0
            l = 0
            while l <= i.count("."):
                domain = i[v+1:]
                if not (domain in graph):
                    graph[domain] = visits
                else:
                    graph[domain] += visits
                v = i.find(".",k)
                k = v + 1
                l += 1
        printable = []
        for j in graph:
            p = str(graph[j]) + " " + j
            printable.append(p)
        return printable