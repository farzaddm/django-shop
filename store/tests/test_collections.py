from rest_framework import status
from store.models import Collection
from model_bakery import baker
import pytest


@pytest.fixture
def create_collection(api_client):
    # because if we define collection in the first func the
    # pytest thinks it is a fixture
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymouse_return_401(self, create_collection):
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_Admin_return_403(self, authenticate, create_collection):
        authenticate()
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, authenticate, create_collection):
        authenticate(is_staff=True)
        response = create_collection({'title': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_return_201(self, authenticate, create_collection):
        authenticate(is_staff=True)
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_return_200(self, api_client):
        collection = baker.make(Collection)
        response = api_client.get(f'/store/collections/{collection.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }

    def test_if_collection_not_exists_return_404(self, api_client):
        response = api_client.get(f'/store/collections/1/')
        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestUpdateCollection:
    def test_if_user_not_admin_return_403(self, authenticate, api_client):
        authenticate()
        response = api_client.patch(f'/store/collections/1/', {'title': 'b'})
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_not_exists_return_404(self, authenticate, api_client):
        authenticate(is_staff=True)
        response = api_client.patch(f'/store/collections/1/', {'title': 'b'})
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_exists_and_data_valid_return_200(self, authenticate, api_client):
        authenticate(is_staff=True)
        collection = baker.make(Collection)
        response = api_client.patch(f'/store/collections/{collection.id}/', {'title': 'b'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'b'
    
    def test_if_data_invalid_return_400(self, authenticate, api_client):
        authenticate(is_staff=True)
        collection = baker.make(Collection)
        response = api_client.put(f'/store/collections/{collection.id}/', {'wrong': 'b'})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
