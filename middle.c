// return the middle node of a linked list
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* middleNode(struct ListNode* head){
    struct ListNode *aux = head;
    int count = 0;
    while (aux != NULL){
        count++;
        aux = aux->next;
    }
    int middle = count/2;
    aux = head;
    for (int i = 0; i < middle; i++){
        aux = aux->next;
    }
    return aux;
}