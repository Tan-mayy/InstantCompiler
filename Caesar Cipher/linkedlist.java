public class linkedlist
{

public static void main(String Args[]){
    node n1 = new node(10);
    node n2 = new node(20);
    node n3 = new node(30);
    node n4 = new node(40);
    node n5 = new node(50);
    n1.next = n2;
    n2.next = n3;
    n3.next = n4;
    n4.next = n5;
    n4.next = null;

    for (int i = 0; i < 6; i++){
        System.out.println(n1.data);
    }
}

}