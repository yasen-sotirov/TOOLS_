from models.test_group import TestGroup


class ApplicationData():
    def __init__(self):

        self._test_groups: list[TestGroup] = []                                           

    @property
    def groups(self):
        return tuple(self._test_groups)

    def create_testGroup(self, id, name):

        if self.testGroup_does_exist(name):
            raise ValueError("TestGroup already exists!")

        testgroup = TestGroup(id, name)
        self._test_groups.append(testgroup)

    def testGroup_does_exist(self, name):
        for x in self._test_groups:

            if name == x.name:

                raise ValueError('TestGroup with this name already exists!')

    def find_group_by_id(self, id):

        for x in self._test_groups:

            if id == x.id:

                return x

    def find_test_by_id(self, id):

        for x in self._test_groups:

            for j in x._tests:

                if id == j.id:

                    return j

    def test_report(self, id):

        group = self._test_groups

        runs = 0

        pas = 0

        fail = 0

        runtime = 0

        for x in group:

            for j in x._tests:

                for i in j._test_runs:

                    runs += 1

                    if i.test_result == 'pass':
                        pas += 1

                    else:

                        fail += 1

                    runtime += int(i.runtime_ms)

                return f"#{id}. [{j.description}]: {runs} runs\n- Passing: {pas}\n- Failing: {fail}\n- Total runtime: {runtime}ms\n- Average runtime: {runtime/runs}"


    def view_group(self,id):
        
        group = self._test_groups

        for x in group:

            if id == x.id:

                name_group = x._name

                test_count = len(x._tests)

            else:

                raise ValueError('Groud doesnt exists')

            for tests in x._tests:

                print(f'#{id}. {name_group} ({test_count} tests)\n#{tests._id}.[{tests._description}]: {len(tests._test_runs)}')