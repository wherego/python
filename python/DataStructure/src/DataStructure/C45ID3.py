


import math;

global_list_mark = [];
class tree_node(object):
    def __init__(self):

            self.value = -1;

            self.childs = [];

def LoadSet():
        dataMat = []; labelMat = [];
        fr = open('testSet.txt');
        for line in fr.readlines():
            lineArr = line.strip().split();
            dataMat.append([float(lineArr[0]), float(lineArr[1]), float(lineArr[2]), float(lineArr[3])]);
            labelMat.append(int(lineArr[4]));
        fr.close();
        return mat(dataMat),mat(labelMat).transpose();

def if_only_contain_one_class(label):
        if len(label) < 2:
            return True;
        for i in range(len(label)):
            if label[0][0] != label[i][0]:
                return False;
        return True;

def calculate_empirical_entropy(data_set,label):
        m,n = shape(data_set);

        if if_only_contain_one_class(label):
            return 0.0;
        c1 = c2 =0.0;
        for i in range(m):
            if label[i]:
                c1 += 1;
            else:
                c2 += 1;
        return -(c1/m)*math.log(c1/m)-(c2/m)*math.log(c2/m);
def calculate_conditional_entropy(data_set,label,mark = False):
        m,n = shape(data_set);
        conditional_entropy = [];
        information_gain_ratio = [];

        for j in range(n):
            if j in global_list_mark:
                continue;
            tmp_class = {};
            feature_j_entropy = 0.0;
            class_j_entropy = 0.0;
            for i in range(m):
                tmp = data_set[i][j];
                if tmp_class.has_key(tmp):
                    tmp_class[tmp].append(i);
                else:
                    tmp_list = [];
                    tmp_list.append(i);
                    tmp_class[tmp] = tmp_list;

            for i in tmp_class.keys():
                Di = float(len(tmp_class[i]));
                Dik1 = Dik2 = 0.0;
                for k in tmp_class[i]:
                    if label[k][0]:
                        Dik1 += 1.0;
                    else:
                        Dik2 += 1.0;
                if Dik1 == 0 or Dik2 == 0:
                    continue;
                else:
                    feature_j_entropy -= ((Dik1/Di)*math.log(Dik1/Di)+\
                                          (Dik2/Di)*math.log(Dik2/Di))*(Di/m);
                    if mark:
                        class_j_entropy += Di/m;
            if mark:
                if class_j_entropy == 0.0:
                    information_gain_ratio.append(0.0);
                else:
                    information_gain_ratio.append(feature_j_entropy/class_j_entropy);
            else:
                conditional_entropy.append(feature_j_entropy);
        if mark:
            return information_gain_ratio;
        else:
            return conditional_entropy;
def calculate_infomation_gain(data_set,label):
        empirical_entropy = calculate_empirical_entropy(data_set,label);
        conditional_entropy = calculate_conditional_entropy(data_set,label);
        print("(empirical_entropy,conditional_entropy): ",empirical_entropy,conditional_entropy);
        information_gain = {};
        k=0;
        for i in conditional_entropy:
            information_gain[empirical_entropy-i] = k;
            k += 1;
        print("information_gain: ",information_gain);
        return information_gain;


def calculate_max_infomation_gain(data_set,label):
        if if_only_contain_one_class(label):
            return -1;

        tmp = calculate_infomation_gain(data_set,label);
        p = max(tmp)
        return tmp[p];


def calculate_max_infomation_gain_ratio(data_set,label):
        if if_only_contain_one_class(label):
            return -1;
        tmp = calculate_conditional_entropy(data_set,label,True);
        print("information_gain_ratio: ",tmp);
        j = max(tmp);
        for i in range(len(tmp)):
            if tmp[i] == j:
                return i+1;
        return -1;
def split_data_set(data_set,label):
        if if_only_contain_one_class(label):
            return 0,-1;
        m,n = shape(data_set);
        feature = calculate_max_infomation_gain_ratio(data_set,label);
        global_list_mark.append(feature);

        feature_set = {};
        for i in range(m):
            tmp = data_set[i][feature];
            if feature_set.has_key(tmp):
                feature_set[tmp].append(i);
            else:
                tmp_list = [];
                tmp_list.append(i);
                feature_set[tmp] = tmp_list;
        return (feature_set,feature);
def reconstruct_data(root,data_set,label):

        data_matrix = [];
        label_matrix = [];
        if if_only_contain_one_class(label):
            return data_matrix,label_matrix;
        feature_set,j = split_data_set(data_set,label);
        root.value = j;
        m,n = shape(data_set);
        print("feature: ",j);
        for key in feature_set.keys():
            tmp_list = feature_set[key];
            tmp_m = len(tmp_list);
            tmp_matrix = zeros((tmp_m,n));
            tmp_label = zeros((tmp_m,1));
            row = 0;
            for k in tmp_list:
                col = 0;
                for i in range(n):
                    tmp_matrix[row][col] = data_set[k][i];
                    col += 1;
                tmp_label[row] = label[k];
                row += 1;
            label_matrix.append(tmp_label);
            data_matrix.append(tmp_matrix);
        return data_matrix,label_matrix;
def decide_tree(root,data_set,label,depth=24):
        data_list,label_list = [],[];
        if depth < 1 or if_only_contain_one_class(label):
            return 0;
        depth -= 1;
        data_list,label_list = reconstruct_data(root,data_set,label);
        for i in range(len(data_list)):
            child = tree_node();
            decide_tree(child,data_list[i],label_list[i],depth);
            root.childs.append(child);

def post_traversal(root):
        if (not root) or len(root.childs) == 0:
            return 0;
        for i in range(len(root.childs)):
            if root.childs[i].value > 0:
                print ("father feature: ",root.value," child feature: ",root.childs[i].value);
        for child in root.childs:
            post_traversal(child);
def perform_decision_tree():
        data_set,label = LoadSet();
        root = tree_node();
        data_set = data_set.getA();
        label = label.getA();
        decide_tree(root,data_set,label);
        print("root: ",root.value);
        post_traversal(root);

